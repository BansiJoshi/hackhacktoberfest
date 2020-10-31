puts "Enter the nth term: "

sum = 0
n = gets.chomp.to_i
for i in (1..n)
  if i % 2 == 0
    sum += i
  end
end
puts "The sum of the even numbers between 1 and #{n} is: #{sum}"
