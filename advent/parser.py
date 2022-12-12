from typing import Any, List

def take(it, n):
    return [next(it) for _ in range(n)]

class ParserBase:
    def parse(self, fh):
        return next(fh)

    def __rshift__(self, wrapper):
        return WrappedParser(self, wrapper)

class ParserSkip(ParserBase):
    def parse(self, fh):
        try: next(fh)
        except StopIteration: return

def to_parser(p):
    if p == Any: return ParserSkip()
    if isinstance(p, ParserBase): return p
    if callable(p): return FParser(p)
    if type(p) == list or type(p) == tuple: return SeqParser(p)
    raise TypeError(f"Can't coerce {type(p)} into a Parser")

class SeqParser(ParserBase):
    def __init__(self, sequence: List[ParserBase]) -> None:
        self.seq = [to_parser(p) for p in sequence]
    
    def parse(self, fh):
        output = []
        for p in self.seq:
            try:
                if isinstance(p, ParserSkip):
                    p.parse(fh)
                else:
                    output.append(p.parse(fh))
            except StopIteration:
                raise StopIteration

        if output:
            if len(output) == 1:
                return output[0]
            return output
        else:
            return None

class StarParser(ParserBase):
    def __init__(self, *inner_sequence) -> None:
        if inner_sequence:
            if len(inner_sequence) == 1:
                self.inner = to_parser(inner_sequence[0])
            else:
                self.inner = to_parser(inner_sequence)
        else:
            raise ValueError("Can't star nothing")
    
    def parse(self, fh):
        def loop():
            while True:
                try:
                    
                    yield self.inner.parse(fh)
                except StopIteration:
                    break
        return list(loop())

class FParser(ParserBase):
    def __init__(self, f) -> None:
        self.f = f

    def parse(self, fh):
        return self.f(fh)

class LabeledParser: pass

class Split(ParserBase):
    def __init__(self, by, inner):
        self.by = by
        self.inner = to_parser(inner)
    
    def parse(self, fh):
        e = next(fh)
        if type(e) == str:
            return self.inner.parse(iter(e.split(self.by)))
        # def splitter():
        #     for se in e:
        #         if se == self.by
        raise NotImplementedError("Not implemented for non-strings")


class Parser(ParserBase):
    def __init__(self, *pat):
        if pat:
            if len(pat) > 1:
                self.inner = SeqParser(pat)
            elif callable(pat[0]):
                self.inner = FParser(pat[0])
            else:
                self.inner = pat[0]
        else:
            self.inner = ParserSkip()

    def parse(self, fh):
        return self.inner.parse(fh)
    

class WrappedParser(ParserBase):
    def __init__(self, inner, wrapper):
        self.inner = inner
        self.wrapper = wrapper

    def parse(self, fh):
        return self.wrapper(self.inner.parse(fh))

