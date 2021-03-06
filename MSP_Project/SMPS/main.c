/* Contolador para seguidor solar e controlador dos motores da placa
*/

#include <msp430.h> 
#include "mspFunctions.h"



int main(void){
	WDTCTL = WDTPW | WDTHOLD;                       // Turn off the watchdog timer

	/*Setting the clock to 8Mhz*/
	BCSCTL1 = CALBC1_8MHZ;
	DCOCTL = CALDCO_8MHZ;
	
	/* Initializing variable to store the ADCs */
	unsigned int adc_mesure[ADC_CHANNELS] = { 0, 0 };
	volatile int mean = 0;

	ADC_Init(); // Starting the ADC
	__enable_interrupt(); // Enable interrupts.

	while(1){
	    ADC10CTL0 &= ~ENC;
        while (ADC10CTL1 & BUSY);                   // Wait if ADC10 core is activate
        ADC10SA = (unsigned int)adc_mesure;            // Data buffer start

        __delay_cycles(1000); // Wait for ADC Ref to settle
        ADC10CTL0 |= ENC + ADC10SC; // Sampling and conversion start
        __bis_SR_register(CPUOFF + GIE); // LPM0 with interrupts enabled

        mean = adc_mesure[1] - adc_mesure[0];
	}


	return 0;
}
