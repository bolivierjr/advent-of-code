defmodule Day01 do
  defp get_input() do
    case File.read("input.txt") do
      {:ok, inputs} ->
        inputs
        |> String.replace("\r", "")
        |> String.split("\n")
        |> Enum.map(&String.to_integer/1)

      {:error, _} ->
        throw("File not found")
    end
  end

  def required_fuel(mass) do
    trunc(mass / 3) - 2
  end

  def total_required_fuel(mass) do
    fuel = required_fuel(mass)
    if fuel <= 0, do: 0, else: fuel + total_required_fuel(fuel)
  end

  def part_1(masses) do
    masses
    |> Enum.map(&required_fuel/1)
    |> Enum.sum()
  end

  def part_2(masses) do
    masses
    |> Enum.map(&total_required_fuel/1)
    |> Enum.sum()
  end

  def run do
    try do
      input = get_input()
      IO.puts("The solution to part 1 is: #{part_1(input)}")
      IO.puts("The solution to part 2 is: #{part_2(input)}")
    catch
      input -> exit("Error: #{input}")
    end
  end
end

Day01.run()
