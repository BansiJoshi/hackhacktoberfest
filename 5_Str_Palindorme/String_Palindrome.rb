# This method is strict in that it case sensitive and cares about characters
# including empty spaces

def palindrome(string)
  if string == string.reverse
    puts "The word #{string} is a palindrome."
  else
    puts "The word #{string} is not a palindrome."
  end
end

puts "Please type any word you like"
string = gets.chomp
palindrome(string)
