import sqlite3 as sql

conn = sql.connect('car_base.db')

conn.execute('CREATE TABLE Base (Year INT,\
Make Char(30),\
Model Char(30),\
Trim Char(30),\
Manf_In Char(20),\
Seq_Num INT,\
Body_Type CHAR(25),\
Engine Char(30),\
Trans_Short Char(11),\
Transmission CHAR(30),\
Drive Char(11),\
Fuel_Size Char(15),\
Mpg_City CHAR(30),\
Mpg_Hwy CHAR(30),\
Abs CHAR(11),\
Steering CHAR (15),\
Front_Brake Char(11),\
Rear_Brake Char(11),\
Turn_Diameter Char(20),\
Front_Susp Char(11),\
Rear_Susp Char(11),\
Front_Spring Char(11),\
Rear_Spring Char(11),\
Tires Char(11),\
Front_Head Char(11),\
Rear_Head Char(11),\
Front_Leg Char(11),\
Rear_Leg Char(11),\
Front_Sho Char(11),\
Rear_Sho Char(11),\
Front_Hip Char(11),\
Rear_Hip Char(11),\
Int_Trim VARCHAR(300),\
Ext_Color VARCHAR(300),\
Weight_Auto Char(11),\
Weight_Man Char(11),\
Length Char(11),\
Width Char(11),\
Height Char(11),\
Wheelbase Char(11),\
Clearance Char(11),\
Front_Track Char(11),\
Rear_Track Char(11),\
Cargo Char(11),\
Wheelwell Char(11),\
Wall Char(11),\
Depth Char(11),\
Seats INT,\
Seats_Opt INT,\
Vol_Pass Char(11),\
Vol_Cargo Char(11),\
Tow_Std Char(11),\
Tow_Max Char(11),\
Payload_Std Char(11),\
Payload_Max Char(11),\
GVWR_Std Char(11),\
GVWR_Max Char(11),\
Dur_Basic CHAR (11),\
Dist_Basic CHAR (11),\
Dur_Pt CHAR (11),\
Dist_Pt CHAR (11),\
Dur_Rust CHAR (11),\
Dist_Rust CHAR (11),\
MSRP Char(15),\
Invoice Char(15),\
Dest_Charge Char(15),\
Child_Lock Char(11),\
Tailgate_Lock CHAR (11),\
Power_Lock CHAR (11),\
Anti_Theft CHAR (11),\
Awd_4wd CHAR(11),\
Abs_Brake CHAR (11),\
Auto_Level CHAR (11),\
Eba CHAR (11),\
Lsd CHAR (11),\
Lock_Diff CHAR (11),\
Trac_Cont CHAR (11),\
Vscs CHAR (11),\
Air_Driver CHAR (11),\
Air_FrontSide CHAR (11),\
Air_FrontHead CHAR (11),\
Air_Pass CHAR (11),\
Air_SideHead CHAR (11),\
Air_Second CHAR (11),\
Air_SecondHead CHAR (11),\
Park_Assistance CHAR (11),\
First_Aid CHAR (11),\
Trunk_AntiTrap CHAR (11),\
Keyless CHAR (11),\
Remote_Ign CHAR (11),\
Ac CHAR (11),\
Ac_Split CHAR (11),\
Cruise CHAR (11),\
Tachometer CHAR (11),\
Tilt CHAR (11),\
Tilt_Col CHAR (11),\
Steer_Heat CHAR (11),\
Steer_Leather CHAR (11),\
Steer_Controls CHAR (11),\
Steer_Tel CHAR (11),\
Adjust_Pedal CHAR (11),\
Wood CHAR (11),\
Tps CHAR (11),\
Trip CHAR (11),\
Amfm CHAR (11),\
Cassette CHAR (11),\
Cd_Player CHAR (11),\
Cd_Changer CHAR (11),\
Dvd CHAR (11),\
Voice CHAR (11),\
Nav CHAR (11),\
Second_Sound CHAR (11),\
Sub CHAR (11),\
Tele CHAR (11),\
Seat_Power CHAR (11),\
Seat_Cool CHAR (11),\
Seat_Heat CHAR (11),\
Seat_Lumbar CHAR (11),\
Seat_Memory CHAR (11),\
Split_Bench CHAR (11),\
Seat_Leather CHAR (11),\
Seat_Pass_Power CHAR (11),\
Second_Fold CHAR (11),\
Second_Heat CHAR (11),\
Second_Adjust CHAR (11),\
Second_Remove CHAR (11),\
Third_Remove CHAR (11),\
Cargo_Cover CHAR (11),\
Cargo_Tie CHAR (11),\
Cargo_Net CHAR (11),\
Ext_Rack CHAR (11),\
Bed_Liner CHAR (11),\
Sunroof_Power CHAR (11),\
Top_Remove CHAR (11),\
Sunroof_Man CHAR (11),\
Light_Auto CHAR (11),\
Light_Day CHAR (11),\
Light_Fog CHAR (11),\
Light_Hid CHAR (11),\
Light_Cargo CHAR (11),\
Running CHAR (11),\
Front_Dam CHAR (11),\
Spoiler CHAR (11),\
Skid CHAR (11),\
Splash CHAR (11),\
Deflector CHAR (11),\
Power_Van CHAR (11),\
Power_Trunk CHAR (11),\
Alloy CHAR (11),\
Chrome CHAR (11),\
Spare_Full CHAR (11),\
Run_Flat CHAR (11),\
Steel CHAR (11),\
Power_Window CHAR (11),\
Mirror_ExtElec CHAR (11),\
Mirror_Glass CHAR (11),\
Mirror_Heat CHAR (11),\
Mirror_IntElec CHAR (11),\
Mirror_ExtPower CHAR (11),\
Tint CHAR (11),\
Wiper_Inter CHAR (11),\
Wiper_Sense CHAR (11),\
Window_Defog CHAR (11),\
Wiper_Rear CHAR (11),\
Window_Slide CHAR (11),\
Tow_Hitch CHAR (11),\
Tow_Prep CHAR (11),\
Engine_Comp CHAR (11),\
Fuel_Type CHAR (11),\
Market_Percep CHAR (11),\
Doors CHAR (11),\
Style CHAR (11),\
Type CHAR (11),\
Engine_Cyl CHAR (11),\
Engine_Disp CHAR (11),\
Size CHAR (11),\
Engine_Hp CHAR (11),\
Trims CHAR (11),\
Drivetrain CHAR (15),\
PRIMARY KEY(Year,Make,Model,Trim,Engine))')

conn.close()
