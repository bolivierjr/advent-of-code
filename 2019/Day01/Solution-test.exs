ExUnit.start

defmodule Day01Test do
  use ExUnit.Case

  test "part1_required_fuel" do
    # Test the required fuel for each input of mass.
    %{12 => 2, 14 => 2, 1969 => 654, 100_756 => 33_583}
    |> Enum.each(fn {input, expected} ->
      assert Day01.required_fuel(input) == expected
    end)
  end

  test "part1_total_fuel" do
    assert Day01.part_1([12, 14, 1969, 100_756]) == 34_241
  end

  test "part2_required_fuel" do
    # Test the required fuel for each input of mass.
    %{12 => 2, 14 => 2, 1969 => 966, 100_756 => 50_346}
    |> Enum.each(fn {input, expected} ->
      assert Day01.total_required_fuel(input) == expected
    end)
  end

  test "part2_total_fuel" do
    assert Day01.part_2([12, 14, 1969, 100_756]) == 51_316
  end
end
