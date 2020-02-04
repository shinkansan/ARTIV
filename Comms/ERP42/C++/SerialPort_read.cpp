        /*====================================================================================================*/
        /* Serial Port Programming in C (Serial Port Read)                                                    */
	/* Non Cannonical mode                                                                                */
	/*----------------------------------------------------------------------------------------------------*/
        /* Program reads a string from the serial port at 9600 bps 8N1 format                                 */
	/* Baudrate - 9600                                                                                    */
	/* Stop bits -1                                                                                       */
	/* No Parity                                                                                          */
        /*----------------------------------------------------------------------------------------------------*/
	/* Compiler/IDE  : gcc 4.6.3                                                                          */
	/* Library       :                                                                                    */
	/* Commands      : gcc -o serialport_read serialport_read.c                                           */
	/* OS            : Linux(x86) (Linux Mint 13 Maya)(Linux Kernel 3.x.x)                                */                              
	/* Programmer    : Rahul.S                                                                            */
	/* Date	         : 21-December-2014                                                                   */
	/*====================================================================================================*/

	/*====================================================================================================*/
	/* www.xanthium.in										      */
	/* Copyright (C) 2014 Rahul.S                                                                         */
	/*====================================================================================================*/

	/*====================================================================================================*/
	/* Running the executable                                                                             */
	/* ---------------------------------------------------------------------------------------------------*/ 
	/* 1) Compile the  serialport_read.c  file using gcc on the terminal (without quotes)                 */
        /*                                                                                                    */
	/*	" gcc -o serialport_read serialport_read.c "                                                  */
	/*                                                                                                    */
        /* 2) Linux will not allow you to access the serial port from user space,you have to be root.So use   */
        /*    "sudo" command to execute the compiled binary as super user.                                    */
        /*                                                                                                    */
        /*       "sudo ./serialport_read"                                                                     */
	/*                                                                                                    */
	/*====================================================================================================*/

	/*====================================================================================================*/
	/* Sellecting the Serial port Number on Linux                                                         */
	/* ---------------------------------------------------------------------------------------------------*/ 
	/* /dev/ttyUSBx - when using USB to Serial Converter, where x can be 0,1,2...etc                      */
	/* /dev/ttySx   - for PC hardware based Serial ports, where x can be 0,1,2...etc                      */
        /*====================================================================================================*/
	
	/*-------------------------------------------------------------*/
    	/* termios structure -  /usr/include/asm-generic/termbits.h    */ 
	/* use "man termios" to get more info about  termios structure */
	/*-------------------------------------------------------------*/

    	#include <stdio.h>
    	#include <fcntl.h>   /* File Control Definitions           */
    	#include <termios.h> /* POSIX Terminal Control Definitions */
    	#include <unistd.h>  /* UNIX Standard Definitions 	   */ 
    	#include <errno.h>   /* ERROR Number Definitions           */
	#include <iostream>
        using namespace std;
	int main(void)
    	{
        	int fd;/*File Descriptor*/
		
		printf("\n +----------------------------------+");
		printf("\n |        Serial Port Read          |");
		printf("\n +----------------------------------+");

		/*------------------------------- Opening the Serial Port -------------------------------*/

		/* Change /dev/ttyUSB0 to the one corresponding to your system */

        	fd = open("/dev/ttyUSB1",O_RDWR | O_NOCTTY);	/* ttyUSB0 is the FT232 based USB2SERIAL Converter   */
			   					/* O_RDWR   - Read/Write access to serial port       */
								/* O_NOCTTY - No terminal will control the process   */
								/* Open in blocking mode,read will wait              */
									
									                                        
									
        	if(fd == -1)						/* Error Checking */
            	   printf("\n  Error! in Opening ttyUSB0  ");
        	else
            	   printf("\n  ttyUSB0 Opened Successfully ");

	
		/*---------- Setting the Attributes of the serial port using termios structure --------- */
		
		struct termios SerialPortSettings;	/* Create the structure                          */

		tcgetattr(fd, &SerialPortSettings);	/* Get the current attributes of the Serial port */

		/* Setting the Baud rate */
		cfsetispeed(&SerialPortSettings,B115200); /* Set Read  Speed as 9600                       */
		cfsetospeed(&SerialPortSettings,B115200); /* Set Write Speed as 9600                       */

		/* 8N1 Mode */
		SerialPortSettings.c_cflag &= ~PARENB;   /* Disables the Parity Enable bit(PARENB),So No Parity   */
		SerialPortSettings.c_cflag &= ~CSTOPB;   /* CSTOPB = 2 Stop bits,here it is cleared so 1 Stop bit */
		SerialPortSettings.c_cflag &= ~CSIZE;	 /* Clears the mask for setting the data size             */
		SerialPortSettings.c_cflag |=  CS8;      /* Set the data bits = 8                                 */
		
		SerialPortSettings.c_cflag &= ~CRTSCTS;       /* No Hardware flow Control                         */
		SerialPortSettings.c_cflag |= CREAD | CLOCAL; /* Enable receiver,Ignore Modem Control lines       */ 
		
		
		SerialPortSettings.c_iflag &= ~(IXON | IXOFF | IXANY);          /* Disable XON/XOFF flow control both i/p and o/p */
		SerialPortSettings.c_iflag &= ~(ICANON | ECHO | ECHOE | ISIG);  /* Non Cannonical mode                            */

		SerialPortSettings.c_oflag &= ~OPOST;/*No Output Processing*/
		
		/* Setting Time outs */
		SerialPortSettings.c_cc[VMIN] = 10; /* Read at least 10 characters */
		SerialPortSettings.c_cc[VTIME] = 0; /* Wait indefinetly   */


		if((tcsetattr(fd,TCSANOW,&SerialPortSettings)) != 0) /* Set the attributes to the termios structure*/
		    printf("\n  ERROR ! in Setting attributes");
		else
                    printf("\n  BaudRate = 115200 \n  StopBits = 1 \n  Parity   = none");
			
	        /*------------------------------- Read data from serial port -----------------------------*/

		tcflush(fd, TCIFLUSH);   /* Discards old data in the rx buffer            */

		char read_buffer[128];   /* Buffer to store the data received              */
		int  bytes_read = 0;    /* Number of bytes read by the read() system call */
 		int i = 0;

		bytes_read = read(fd,&read_buffer,128); /* Read the data                   */
		
		while(1){
		cout << "RX Input[" << bytes_read << "]" << endl <<  read_buffer << endl;
		}
		close(fd); /* Close the serial port */
		return 0;
    	}

