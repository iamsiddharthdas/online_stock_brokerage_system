#include<stdio.h>
#include<time.h>
int main()
{
 int stock_quantity, client_id, brokerage = 45;
 float stock_price, total;
 char choice, stock_name[20], client_name[20];
 time_t t;
 time(&t);

 printf("Enter Client ID   : ");
 scanf("%d",&client_id);

 printf("Enter Client Name : ");
 scanf("%s", client_name);

 printf("Enter Stock Name  : ");
 scanf("%s", stock_name);

 printf("Enter Stock Quantity : ");
 scanf("%d", &stock_quantity);

 printf("Enter Stock Price    : ");
 scanf("%f", &stock_price);



BACK:
 printf("Enter your choice (B for Buy, S for Sell):");
 scanf(" %c", &choice);
 if(choice!='B' && choice!='S')
 {
  printf("\n"); goto BACK;
 }
 total = stock_quantity * stock_price;
 printf("Collect Your Bill As Under...\n");
 printf("========================================\n");
 printf("      STOCK BROKER - CLIENT BILL\n");
 printf("      --------------------------\n");
 printf("Date and Time :%s",ctime(&t));
 printf("Client ID and Name : %d, %s\n",client_id, client_name);
 printf("----------------------------------------\n");
 printf("Stock Name\t\t : %s \n", stock_name);
 printf("Stock Quantity\t\t : %d\n", stock_quantity);
 printf("Stock Price\t\t : %0.2f\n", stock_price);
 printf("----------------------------------------\n");
 printf("Total Stock Transaction Amount = %0.2f\n", total);
 if(choice=='B')
  printf("You will pay us INR %0.2f.\n", total+brokerage);
 if(choice=='S')
  printf("We will pay you INR %0.2f.\n", total-brokerage);
 printf("========================================");

 return 0;
}
