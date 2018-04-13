/*
 * mspFunctions.h
 *
 *  Created on: 13 de abr de 2018
 *      Author: Arnoldo Thiago Monteiro Lima
 */

#ifndef MSPFUNCTIONS_H_
#define MSPFUNCTIONS_H_

#define IN_AD BIT1 | BIT4
#define IN_AD_CH INCH_1

void ADC_Init(void){
    /* Configure the control register 0
     * SERF_X      - Select Reference.
     * ADC10SHT_X  - Sample and Hold Time.  This adjust how many clock cycles the sampling period will be.
     * ADC10ON     - ADC10 On.
     * */
    ADC10CTL0 = SREF_0 + ADC10SHT_0 + ADC10ON;

    /* Configure the control register 1
     * IN_AD_CH    -
     * ADC10DIV_0  - Clock Divider.  Allows the chosen clock source used for the ADC to be divided down. (Divided by 1)
     * ADC10SSEL_3 - Clock Source Select. (SMCLK)
     * CONSEQ_0    - Conversion Sequence Mode. (Single-channel-single-conversion)
     * SHS_0       - Sample and Hold Source Select.
     * */
    ADC10CTL1 = INCH_2 + ADC10DIV_0 + ADC10SSEL_3 + CONSEQ_0 + SHS_0;

    /*2 conversions*/
    ADC10DTC1 = 0x02;

    /*Disable digital I/O on P1.0 to P1.1*/
    ADC10AE0 |= 0x02;

    /*Enable the input register 0*/
    ADC10AE0 = BIT0 | BIT4;
}

#endif /* MSPFUNCTIONS_H_ */
