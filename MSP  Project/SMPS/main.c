/* Contolador para seguidor solar e controlador dos motores da placa
*/

#include <msp430.h> 
#include "mspFunctions.h"

int main(void){
    /*Turn off the watchdog timer*/
	WDTCTL = WDTPW | WDTHOLD;

	/*Setting the clock to 8Mhz*/
	BCSCTL1 = CALBC1_8MHZ;
	DCOCTL = CALDCO_8MHZ;
	
	return 0;
}
