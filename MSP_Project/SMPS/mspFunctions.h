/*
 * mspFunctions.h
 *
 *  Created on: 13 de abr de 2018
 *      Author: Arnoldo Thiago Monteiro Lima
 */

#ifndef MSPFUNCTIONS_H_
#define MSPFUNCTIONS_H_

/* 5 channels of ADC */
#define ADC_CHANNELS 2

/* Define the port to ADC */
#define AD_UP   BIT0
#define AD_DOWN BIT3

/* Function to Initialize the ADC */
void ADC_Init(void)
{
    /* Configure the control register 0
     * SERF_X      - Select Reference.
     * ADC10SHT_X  - Sample and Hold Time.  This adjust how many clock cycles the sampling period will be.
     * ADC10ON     - ADC10 On.
     * MSC         - Multiple sample and conversion.
     * */
    ADC10CTL0 = SREF_0 + ADC10SHT_0 + ADC10ON + MSC + ADC10IE;

    /* Configure the control register 1
     * IN_AD_CH    -
     * ADC10DIV_0  - Clock Divider.  Allows the chosen clock source used for the ADC to be divided down. (Divided by 1)
     * ADC10SSEL_3 - Clock Source Select. (SMCLK)
     * CONSEQ_3    - Conversion Sequence Mode. (Single-channel-single-conversion)
     * SHS_0       - Sample and Hold Source Select.
     * */
    ADC10CTL1 = INCH_4 + ADC10DIV_0 + ADC10SSEL_3 + CONSEQ_3 + SHS_0;

    /*The number of transfers in each block*/
    ADC10DTC1 = ADC_CHANNELS;

    /*Choosing the port to ADC*/
    ADC10AE0 = AD_UP + AD_DOWN;

}

/* ADC10 interrupt service routine */
#pragma vector=ADC10_VECTOR
__interrupt void ADC10_ISR (void){
   __bic_SR_register_on_exit(CPUOFF); // Return to active mode
}

#endif /* MSPFUNCTIONS_H_ */
