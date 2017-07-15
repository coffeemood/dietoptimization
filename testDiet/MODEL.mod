/*********************************************
 * OPL 12.6.0.0 Model
 * Author: Vicky
 * Creation Date: Mar 21, 2016 at 10:37:11 AM
 *********************************************/

{string} Food = ...;

float cost[Food] = ...; 
float protein[Food] = ...;
float fibre[Food] = ...;
float sugar[Food] = ...;
float satfat[Food] = ...; 

dvar float+ yAmount[Food]; // The amount of food to purchase in units of 100 grams 

minimize
sum(i in Food) cost[i] * yAmount[i];

subject to {
 

sum(i in Food) protein[i]*yAmount[i] >= 45;
   

sum(i in Food) fibre[i]*yAmount[i] >= 25;


sum(i in Food) sugar[i]*yAmount[i] >= 0.43;


sum(i in Food) satfat[i]*yAmount[i] <= 12;

forall (i in Food) yAmount[i] <= 3;

}
