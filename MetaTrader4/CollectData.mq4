//+------------------------------------------------------------------+
//|                                                  CollectData.mq4 |
//|                                                    Le Quang Vinh |
//|                                             https://www.home.com |
//+------------------------------------------------------------------+
#property copyright "Le Quang Vinh"
#property link      "https://www.home.com"
#property version   "1.00"
#property strict
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//--- create timer
   EventSetTimer(60);

   int bar_num = Bars(_Symbol, 0);
   Print("Bar number: ", bar_num);
   // Time, Open, High, Low, Close, Volumn
   // MA 5-10-20-50-8-13-21
   // MO 5-8-10-12-13-21
   // RSI 5-8-9-10-12-13-14-21-25
   int file_handle = FileOpen("Data.txt", FILE_WRITE|FILE_TXT);
   Print(file_handle);
   int bytes = FileWrite(file_handle, "Time;Open;High;Low;Close;Volumn;MA5;MA10;MA20;MA50;MA8;MA13;MA21;MO5;MO8;MO10;MO12;MO13;MO21;RSI5;RSI8;RSI9;RSI10;RSI12;RSI13;RSI14;RSI21;RSI25");
   
   for (int i = bar_num-1; i >= 0; i--)
   {
      datetime time = iTime(NULL, 0, i);
      double open = iOpen(NULL, 0, i);
      double high = iHigh(NULL, 0, i);
      double low = iLow(NULL, 0, i);
      double close = iClose(NULL, 0, i);
      int volumn = iVolume(NULL, 0, i);
      double MA_5 = iMA(NULL, 0, 5, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_10 = iMA(NULL, 0, 10, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_20 = iMA(NULL, 0, 20, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_50 = iMA(NULL, 0, 50, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_8 = iMA(NULL, 0, 8, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_13 = iMA(NULL, 0, 13, i, MODE_SMA, PRICE_CLOSE, i);
      double MA_21 = iMA(NULL, 0, 21, i, MODE_SMA, PRICE_CLOSE, i);
      double MO_5 = iMomentum(NULL, 0, 5, PRICE_CLOSE, i);
      double MO_8 = iMomentum(NULL, 0, 8, PRICE_CLOSE, i);
      double MO_10 = iMomentum(NULL, 0, 10, PRICE_CLOSE, i);
      double MO_12 = iMomentum(NULL, 0, 12, PRICE_CLOSE, i);
      double MO_13 = iMomentum(NULL, 0, 13, PRICE_CLOSE, i);
      double MO_21 = iMomentum(NULL, 0, 21, PRICE_CLOSE, i);
      double RSI_5 = iRSI(NULL, 0, 5, PRICE_CLOSE, i);
      double RSI_8 = iRSI(NULL, 0, 8, PRICE_CLOSE, i);
      double RSI_9 = iRSI(NULL, 0, 9, PRICE_CLOSE, i);
      double RSI_10 = iRSI(NULL, 0, 10, PRICE_CLOSE, i);
      double RSI_12 = iRSI(NULL, 0, 12, PRICE_CLOSE, i);
      double RSI_13 = iRSI(NULL, 0, 13, PRICE_CLOSE, i);
      double RSI_14 = iRSI(NULL, 0, 14, PRICE_CLOSE, i);
      double RSI_21 = iRSI(NULL, 0, 21, PRICE_CLOSE, i);
      double RSI_25 = iRSI(NULL, 0, 25, PRICE_CLOSE, i);
      
      string format = ";%G;%G;%G;%G;%d;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G;%G";
      string out = TimeToString(time, TIME_DATE);
      out += StringFormat(format, open, high, low, close, volumn,
                           MA_5, MA_10, MA_20, MA_50, MA_8, MA_13, MA_21,
                           MO_5, MO_8, MO_10, MO_12, MO_13, MO_21,
                           RSI_5, RSI_8, RSI_9, RSI_10, RSI_12, RSI_13, RSI_14, RSI_21, RSI_25);
      bytes = FileWrite(file_handle, out);
   }
   FileClose(file_handle);
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
   
  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {
//---
   
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
