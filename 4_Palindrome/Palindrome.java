class Palindrome{
 public static void main(String args[]){  
  int a,sum=0,temp;    
  int n=121;
  temp=n;    
  while(n>0){    
   a=n%10;  //getting remainder  
   sum=(sum*10)+a;    
   n=n/10;    
  }    
  if(temp==sum)    
   System.out.println("palindrome number ");    
  else    
   System.out.println("not palindrome");    
}  
}  