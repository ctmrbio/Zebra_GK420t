This catalog contains some driver setings for GK420t Zebra printer.

Tubes barcode printing in CTMR labs goes with help of GK420t barcode printer conected to Windows 10 computers.

To set up GK420t printer to work with Windows 10 you must download and install its drivers from
https://www.zebra.com/us/en/support-downloads/printers/desktop/gk420t.html
page. Then go to newly installed printer driver settings in Windows setup and choose "Printer settings".
In "Printer settings" dialog box go into "Import/Export" tab and import the driver settings from gk420t.drs file of this repository.
After this printer should be able to print tube barcodes on 50x9 mm labels.
If something going wrong then check driver settings manually:
1. On "Options" tab in "Paper Format" choose "mm", in "Size" settings, set the Width to 50 and Height to 990, in "Unprintable Area" settings all values should be zero.
2. On "Advanced Setup" tab all settings of "Adjustment" should be zero. Pree "Other" button to go to "Other settings" dialog box.
3. Here in "Other settings" dialog box in "Commands" settings mark "Enable Passthrough Mode", ensure that "Start sequence" is "${" and "End sequence" is "$)".
Now printer should print correct.
4. All other settings should be in there default state like after initial printer installation.

In common printing is going with help of Notepad++ program. Operator geting barcode zpl file from lims, opens it with Notepad++ and print on GK420t barcode printer which is installed like default printer on lab computer.

There is actually a possibility to print it directly from Windows environment.
For this purpose there is zpl2print.reg file in this repository.
Install it into Windows 10 system by clicking on it. (You should have administrative access).
This will provide a context menu item "print" for *.zpl files.
The command will print the file on default printer with Notepad++ program
(Strange, but it does not work correct with ordinal notepad editor. It does not print an example_barcodes.zpl correctly)

Some ZebraPrinterLanguage*.reg files in this repository are another way to enable printing from context menu, but this approach does not work correctly
I have used information from this pages to set up barcode printing:
https://stackoverflow.com/questions/2123762/add-menu-item-to-windows-context-menu-only-for-specific-filetype
https://docs.microsoft.com/en-us/windows/win32/shell/app-registration#registering-verbs-and-other-file-association-information
