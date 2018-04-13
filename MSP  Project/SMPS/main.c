/* Contolador para seguidor solar e controlador dos motores da placa
*/

#include <msp430.h> 
#include "mspFunctions.h"

int main(void){
	WDTCTL = WDTPW | WDTHOLD;                       // Turn off the watchdog timer

	/*Setting the clock to 8Mhz*/
	BCSCTL1 = CALBC1_8MHZ;
	DCOCTL = CALDCO_8MHZ;
	
	/*SMCLK = DCO = 8MHz*/
	//BCSCTL2 &= DIVS_4; // SMCLK = DCO/8 = 1MHz

	ADC_Init(); // Starting the ADC
	__enable_interrupt(); // Enable interrupts.

	while(1){
	    ADC10CTL0 &= ~ENC;
        while (ADC10CTL1 & BUSY);                   // Wait if ADC10 core is activate
        ADC10SA = (unsigned int)adc_mesure;            // Data buffer start

        __delay_cycles(1000); // Wait for ADC Ref to settle
        ADC10CTL0 |= ENC + ADC10SC; // Sampling and conversion start
        __bis_SR_register(CPUOFF + GIE); // LPM0 with interrupts enabled
	}


	return 0;
}
