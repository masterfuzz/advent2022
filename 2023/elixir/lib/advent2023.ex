defmodule Advent2023 do
  @moduledoc """
  Documentation for `Advent2023`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Advent2023.hello()
      :world

  """
  def hello do
    :world
  end

  def day1 do 
    contents = File.read!("../inputs/02_small")

    games = contents
    |> String.split("\n")
    |> Enum.filter(&String.trim(&1) != "")
    |> Enum.map(fn game ->
      [game_number, colors] = String.split(game, ":") |> Enum.map(&String.trim/1)

      %{game_number: String.split(game_number), colors: colors}
    end)

    IO.inspect(games)

    
  end
end
