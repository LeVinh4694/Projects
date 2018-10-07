//+------------------------------------------------------------------+
//|                                                 Bollinger_EA.mq4 |
//|                        Copyright 2018, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2018, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict

// Define status
#define DISABLE 0
#define ENABLE  1

// Define empty
#define NONE 0

// Define maximum number of orders
#define LIMIT_ORDER 2

// Define take profit threshold
#define THRESHOLD_POINT 5

// Struct used to store order data
struct ORDER {
   int Order_ID[LIMIT_ORDER];
   int Order_Status[LIMIT_ORDER];
   double Total_Profit;
};
ORDER Order;

// Account variables
double upper_balance = 0;
double lower_balance = 0;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//--- create timer
   EventSetTimer(5);
   
   GetAllOrderInfo();
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//--- destroy timer
   EventKillTimer();
      
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---
   UpdateOrderProfit();
   CloseOrder();
  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {
//---
   UpdateBalanceMargin();
  }
//+------------------------------------------------------------------+
//| Tester function                                                  |
//+------------------------------------------------------------------+
double OnTester()
  {
//---
   double ret=0.0;
//---

//---
   return(ret);
  }
//+------------------------------------------------------------------+
//| ChartEvent function                                              |
//+------------------------------------------------------------------+
void OnChartEvent(const int id,
                  const long &lparam,
                  const double &dparam,
                  const string &sparam)
  {
//---
   
  }
//+------------------------------------------------------------------+

void GetAllOrderInfo()
  {
   Order.Total_Profit = 0;
   for(int i = 0; i < 2; i++)
   {
      if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
      {
         OrderPrint();
         Order.Order_ID[i] = OrderTicket();
         Order.Order_Status[i] = ENABLE;
         double profit = OrderProfit();
         Order.Total_Profit += profit;
      }
      else
      {
         Order.Order_ID[i] = NONE;
         Order.Order_Status[i] = DISABLE;
      }
   }
  }
  
void UpdateOrderProfit()
  {
   Order.Total_Profit = 0;
   for(int i = 0; i < 2; i++)
   {
      if(OrderSelect(Order.Order_ID[i], SELECT_BY_TICKET, MODE_TRADES))
      {
         Order.Total_Profit += OrderProfit();
      }
      else
      {
      }
   }
  }
  
void UpdateBalanceMargin()
  {
   lower_balance = AccountBalance() - Order.Total_Profit;
   upper_balance = AccountBalance() + Order.Total_Profit;
  }
  
void CloseOrder()
  {
   for(int i = 0; i < 2; i++)
   {
      if(OrderSelect(Order.Order_ID[i], SELECT_BY_TICKET, MODE_TRADES))
      {
         if(OP_BUY == OrderType())
         {
            if(0.5 <= OrderProfit())
            {
               if(!OrderClose(Order.Order_ID[i], OrderLots(), Bid, 3))
               {
                  Print("Error code: ", GetLastError());
               }
               else Alert("Order closed: ", Order.Order_ID[i]);
            }
         }
         else if(OP_SELL == OrderType())
         {
            if(0.5 <= OrderProfit())
            {
               if(!OrderClose(Order.Order_ID[i], OrderLots(), Ask, 3))
               {
                  Print("Error code: ", GetLastError());
               }
               else Alert("Order closed: ", Order.Order_ID[i]);
            }
         }
      }
      else
      {
      }
   }
  }