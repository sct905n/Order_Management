from tkinter import *
from tkinter import messagebox, ttk
import time


class Cuaso:
    def __init__(self):
        self.cuaso = Tk()
        self.hienthi()
        self.cuaso.mainloop()


    def hienthi(self):
        self.cuaso.title('Menu')
        #self.cuaso.geometry('1200x1200+100+100')

       

        #tạo label ở giữa và trên cùng cửa sổ
        #hiển thị tên
        self.labelchinh = Label(self.cuaso,bd = 15, font = ('Arial Bold', 30), text = 'Restaurant Management')
        self.labelchinh.pack(pady = 10)
        
        #hiển thị thời gian
        self.localtime = time.asctime(time.localtime(time.time()))
        self.label_thoigian = Label(self.cuaso, bd = 15,  font = ('Arial Bold', 25), text =  self.localtime)
        self.label_thoigian.pack()
        self.time = 'Time purchased:  '
        self.thoi_gian_in_hoa_don = self.time + self.localtime

         #tạo khung chính
        self.khung = Frame(self.cuaso, bd = 10, relief = "raise")
        self.khung.pack()
        

        #hiển thị khung bên trái
        self.khung_trai = Frame(self.khung, bd = 6, relief = 'raise')
        self.khung_trai.pack(side = LEFT)

        #hiển thị khung bên phải
        self.khung_phai = Frame(self.khung, bd = 6, relief = 'raise')
        self.khung_phai.pack(side = RIGHT)

        #hiển thị khung ở giữa bên trên
        self.khung_giuatren = Frame(self.khung, bd = 6, relief = 'raise')
        self.khung_giuatren.pack(side = TOP)
        
        #hiển thị khung ở giữa bên dưới
        self.khung_giuaduoi = Frame(self.khung, bd =6, relief = 'raise')
        self.khung_giuaduoi.pack(side = BOTTOM)
        

        
        #-------------------XỬ LÍ GIAO DIỆN CÁC KHUNG -------------------------------------
        self.monchinh = Label(self.khung_trai, font = ('Arial Bold', 20), text = 'Main dish', bd = 10)
        self.monchinh.grid(row = 0, column = 0)
        self.bang_gia_mon_chinh = Label(self.khung_trai, font = ('Arial Bold', 20), text = 'Price', bd = 10)
        self.bang_gia_mon_chinh.grid(row = 0, column = 1)
        self.so_luong_mon_chinh = Label(self.khung_trai, font = ('Arial Bold', 20), text = 'Amount', bd = 10)
        self.so_luong_mon_chinh.grid(row = 0, column = 2)
        

        self.drink = Label(self.khung_phai, font = ('Arial Bold', 20), text = 'Drinks', bd = 10)
        self.drink.grid(row = 0, column = 0)
        self.bang_gia_do_uong = Label(self.khung_phai, font = ('Arial Bold', 20), text = 'Price', bd = 10)
        self.bang_gia_do_uong.grid(row = 0, column = 1)
        self.so_luong_do_uong = Label(self.khung_phai, font = ('Arial Bold', 20), text = 'Amount', bd = 10)
        self.so_luong_do_uong.grid(row = 0, column = 2)
        

        self.dessert = Label(self.khung_giuatren, font = ('Arial Bold', 20), text = 'Dessert', bd = 10)
        self.dessert.grid(row = 0, column = 0)
        self.bang_gia_trang_mieng = Label(self.khung_giuatren, font = ('Arial Bold', 20), text = 'Price', bd = 10)
        self.bang_gia_trang_mieng.grid(row = 0, column = 1)
        self.bang_gia_trang_mieng = Label(self.khung_giuatren, font = ('Arial Bold', 20), text = 'Amount', bd = 10)
        self.bang_gia_trang_mieng.grid(row = 0, column = 2)

        self.thanhtoan = Label(self.khung_giuaduoi, font = ('Arial Bold', 20), text = 'Pay', bd = 10)
        self.thanhtoan.grid(row = 0, column = 0, columnspan = 2)


      
#------------XỬ LÍ GIAO DIỆN KHUNG TRÁI - KHUNG ĐỒ ĂN-----------------------

        self.var1 = IntVar() #giá trị tương ứng với variable ở combo1
        self.var1.set(0)
        self.var_combo1 = StringVar() #tương ứng với textvariable ở txtcombo1
        self.var_combo1.set('')

        self.var2 = IntVar() 
        self.var2.set(0)
        self.var_combo2 = StringVar() 
        self.var_combo2.set('')

        self.var3 = IntVar() 
        self.var3.set(0)
        self.var_combo3 = StringVar() 
        self.var_combo3.set('')

        self.var4 = IntVar() 
        self.var4.set(0)
        self.var_combo4 = StringVar() 
        self.var_combo4.set('')

        self.var5 = IntVar()
        self.var5.set(0)
        self.var_combo5 = StringVar() 
        self.var_combo5.set('')
        
        self.var6 = IntVar()
        self.var6.set(0)
        self.var_combo6 = StringVar() 
        self.var_combo6.set('')

        self.var7 = IntVar() 
        self.var7.set(0)
        self.var_combo7 = StringVar() 
        self.var_combo7.set('')



#--------Check box đồ ăn-BÊN TRÁI----------------
   
        self.combo1 = Checkbutton(self.khung_trai, text = 'French Fries', variable = self.var1, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo1.grid(row = 1, column = 0, sticky = 'w')
        self.label1 = Label(self.khung_trai, text = '35k', font = ('Arial Bold', 16), bd = 10)
        self.label1.grid(row = 1, column = 1)

        self.txtcombo1 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo1, bd = 5, state = DISABLED)
        self.txtcombo1.grid(row = 1, column = 2)
        

        self.combo2 = Checkbutton(self.khung_trai, text = 'Cheeseburger', variable = self.var2, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo2.grid(row = 2, column = 0, sticky = 'w')
        self.label2 = Label(self.khung_trai, text = '55k', font = ('Arial Bold', 16), bd = 10)
        self.label2.grid(row = 2, column = 1)

        self.txtcombo2 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo2, bd = 5, state = DISABLED)
        self.txtcombo2.grid(row = 2, column = 2)
        
 
        self.combo3 = Checkbutton(self.khung_trai, text = 'Tacos', variable = self.var3, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo3.grid(row = 3, column = 0, sticky = 'w')
        self.label3 = Label(self.khung_trai, text = '40k', font = ('Arial Bold', 16), bd = 10)
        self.label3.grid(row = 3, column = 1)

        self.txtcombo3 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo3, bd = 5, state = DISABLED)
        self.txtcombo3.grid(row = 3, column = 2)
        

        self.combo4 = Checkbutton(self.khung_trai, text = 'Nachos with extra cheese     ', variable = self.var4, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo4.grid(row = 4, column = 0, sticky = 'w')
        self.label4 = Label(self.khung_trai, text = '50k', font = ('Arial Bold', 16), bd = 10)
        self.label4.grid(row = 4, column = 1)

        self.txtcombo4 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo4, bd = 5, state = DISABLED)
        self.txtcombo4.grid(row = 4, column = 2)
        

        self.combo5 = Checkbutton(self.khung_trai, text = 'Mini Burger', variable = self.var5, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo5.grid(row = 5, column = 0, sticky = 'w')
        self.label5 = Label(self.khung_trai, text = '40k', font = ('Arial Bold', 16), bd = 10)
        self.label5.grid(row = 5, column = 1)

        self.txtcombo5 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo5, bd = 5, state = DISABLED)
        self.txtcombo5.grid(row = 5, column = 2)
        

        self.combo6 = Checkbutton(self.khung_trai, text = 'French Toast', variable = self.var6, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo6.grid(row = 6, column = 0, sticky = 'w')
        self.label6 = Label(self.khung_trai, text = '35k', font = ('Arial Bold', 16), bd = 10)
        self.label6.grid(row = 6, column = 1)

        self.txtcombo6 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo6, bd = 5, state = DISABLED)
        self.txtcombo6.grid(row = 6, column = 2)
        

        self.combo7 = Checkbutton(self.khung_trai, text = 'Fire Noodles', variable = self.var7, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_trai)
        self.combo7.grid(row = 7, column = 0, sticky = 'w')
        self.label7 = Label(self.khung_trai, text = '45k', font = ('Arial Bold', 16), bd = 10)
        self.label7.grid(row = 7, column = 1)

        self.txtcombo7 = Entry(self.khung_trai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo7, bd = 5, state = DISABLED)
        self.txtcombo7.grid(row = 7, column = 2)

        

#------------------------XỬ LÝ GIAO DIỆN KHUNG BÊN PHẢI - KHUNG ĐỒ UỐNG---------------------------------------
                          
        self.var8 = IntVar() 
        self.var8.set(0)
        self.var_combo8 = StringVar() 
        self.var_combo8.set('')

        self.var9 = IntVar() 
        self.var9.set(0)
        self.var_combo9 = StringVar() 
        self.var_combo9.set('')

        self.var10 = IntVar()
        self.var10.set(0)
        self.var_combo10 = StringVar()
        self.var_combo10.set('')

        self.var11 = IntVar() 
        self.var11.set(0)
        self.var_combo11 = StringVar() 
        self.var_combo11.set('')

        self.var12 = IntVar() 
        self.var12.set(0)
        self.var_combo12 = StringVar() 
        self.var_combo12.set('')
        
        self.var13 = IntVar() 
        self.var13.set(0)
        self.var_combo13 = StringVar() 
        self.var_combo13.set('')

        self.var14 = IntVar() 
        self.var14.set(0)
        self.var_combo14 = StringVar() 
        self.var_combo14.set('')

        #-----Checkbox đồ uống--- BÊN PHẢI------

        self.combo8 = Checkbutton(self.khung_phai, text = 'Americano    ', variable = self.var8, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo8.grid(row = 1, column = 0, sticky = 'w')
        self.label8 = Label(self.khung_phai, text = '35k', font = ('Arial Bold', 16), bd = 10)
        self.label8.grid(row = 1, column = 1)

        self.txtcombo8 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo8, bd = 5, state = DISABLED)
        self.txtcombo8.grid(row = 1, column = 2)
        

        self.combo9 = Checkbutton(self.khung_phai, text = 'Espresso', variable = self.var9, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo9.grid(row = 2, column = 0, sticky = 'w')
        self.label9 = Label(self.khung_phai, text = '35k', font = ('Arial Bold', 16), bd = 10)
        self.label9.grid(row = 2, column = 1)

        self.txtcombo9 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo9, bd = 5, state = DISABLED)
        self.txtcombo9.grid(row = 2, column = 2)
        

        self.combo10 = Checkbutton(self.khung_phai, text = 'Sprite', variable = self.var10, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo10.grid(row = 3, column = 0, sticky = 'w')
        self.label10 = Label(self.khung_phai, text = '15k', font = ('Arial Bold', 16), bd = 10)
        self.label10.grid(row = 3, column = 1)

        self.txtcombo10 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo10, bd = 5, state = DISABLED)
        self.txtcombo10.grid(row = 3, column = 2)
        

        self.combo11 = Checkbutton(self.khung_phai, text = 'Coke', variable = self.var11, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo11.grid(row = 4, column = 0, sticky = 'w')
        self.label11 = Label(self.khung_phai, text = '15k', font = ('Arial Bold', 16), bd = 10)
        self.label11.grid(row = 4, column = 1)

        self.txtcombo11 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo11, bd = 5, state = DISABLED)
        self.txtcombo11.grid(row = 4, column = 2)
        

        self.combo12 = Checkbutton(self.khung_phai, text = 'Juice', variable = self.var12, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo12.grid(row = 5, column = 0, sticky = 'w')
        self.label12 = Label(self.khung_phai, text = '15k', font = ('Arial Bold', 16), bd = 10)
        self.label12.grid(row = 5, column = 1)

        self.txtcombo12 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo12, bd = 5, state = DISABLED)
        self.txtcombo12.grid(row = 5, column = 2)

        
        self.combo13 = Checkbutton(self.khung_phai, text = 'Soda', variable = self.var13, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo13.grid(row = 6, column = 0, sticky = 'w')
        self.label13 = Label(self.khung_phai, text = '15k', font = ('Arial Bold', 16), bd = 10)
        self.label13.grid(row = 6, column = 1)

        self.txtcombo13 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo13, bd = 5, state = DISABLED)
        self.txtcombo13.grid(row = 6, column = 2)
        

        self.combo14 = Checkbutton(self.khung_phai, text = 'Water', variable = self.var14, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_phai)
        self.combo14.grid(row = 7, column = 0, sticky = 'w')
        self.label14 = Label(self.khung_phai, text = '10k', font = ('Arial Bold', 16), bd = 10)
        self.label14.grid(row = 7, column = 1)

        self.txtcombo14 = Entry(self.khung_phai, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo14, bd = 5, state = DISABLED)
        self.txtcombo14.grid(row = 7, column = 2)

#----------------------XỬ LÍ THANH TOÁN - KHUNG GIỮA BÊN DƯỚI-----------------------
        self.nut_reset = Button(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 10, text = 'RESET', command = self.reset, bd = 6)
        self.nut_reset.grid(row = 1, column = 0)

        self.nut_tongtien = Button(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 10, text = 'TOTAL AMOUNT', command = self.tongtien, bd = 6)
        self.nut_tongtien.grid(row = 2, column = 0)

        Label(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 21,  bg = 'red').grid(row = 2, column = 1)
        

        #self.nut_khoang_cach_tong_tien = Label(self.thanhtoan, font = ('Arial Bold', 16), text = 'xvffd', fg = '#EEEEEE')
        #self.nut_khoang_cach_tong_tien(row = 2, column = 1)

        self.nut_hoadon = Button(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 10, text = 'Print', command = self.Hoadon, bd = 6)
        self.nut_hoadon.grid(row = 3, column = 0)

        self.nut_exit = Button(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 10, text = 'EXIT', command = self.exit, bd = 6)
        self.nut_exit.grid(row = 4, column = 0)


        


#---------------------XỬ LÍ MÓN TRÁNG MIỆNG - KHUNG GIAO DIỆN Ở GIỮA BÊN TRÊN--------------------------------
        self.var15 = IntVar() 
        self.var15.set(0)
        self.var_combo15 = StringVar() 
        self.var_combo15.set('')

        self.var16 = IntVar() 
        self.var16.set(0)
        self.var_combo16 = StringVar() 
        self.var_combo16.set('')

        self.var17 = IntVar()
        self.var17.set(0)
        self.var_combo17 = StringVar()
        self.var_combo17.set('')

        self.var18 = IntVar() 
        self.var18.set(0)
        self.var_combo18 = StringVar() 
        self.var_combo18.set('')

        self.var19 = IntVar() 
        self.var19.set(0)
        self.var_combo19 = StringVar() 
        self.var_combo19.set('')
        
        self.var20 = IntVar() 
        self.var20.set(0)
        self.var_combo20 = StringVar() 
        self.var_combo20.set('')

        

        #-----Checkbox đồ tráng miệng - giữa bên trên

        self.combo15 = Checkbutton(self.khung_giuatren, text = 'Cheesecake', variable = self.var15, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo15.grid(row = 1, column = 0, sticky = 'w')
        self.label15 = Label(self.khung_giuatren, text = '45k', font = ('Arial Bold', 16), bd = 10)
        self.label15.grid(row = 1, column = 1)

        self.txtcombo15 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo15, bd = 5, state = DISABLED)
        self.txtcombo15.grid(row = 1, column = 2)
        

        self.combo16 = Checkbutton(self.khung_giuatren, text = 'Creamy Pudding', variable = self.var16, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo16.grid(row = 2, column = 0, sticky = 'w')
        self.label16 = Label(self.khung_giuatren, text = '30k', font = ('Arial Bold', 16), bd = 10)
        self.label16.grid(row = 2, column = 1)

        self.txtcombo16 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo16, bd = 5, state = DISABLED)
        self.txtcombo16.grid(row = 2, column = 2)
        

        self.combo17 = Checkbutton(self.khung_giuatren, text = 'Brownies', variable = self.var17, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo17.grid(row = 3, column = 0, sticky = 'w')
        self.label17 = Label(self.khung_giuatren, text = '25k', font = ('Arial Bold', 16), bd = 10)
        self.label17.grid(row = 3, column = 1)

        self.txtcombo17 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo17, bd = 5, state = DISABLED)
        self.txtcombo17.grid(row = 3, column = 2)
        

        self.combo18 = Checkbutton(self.khung_giuatren, text = 'Tiramisu', variable = self.var18, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo18.grid(row = 4, column = 0, sticky = 'w')
        self.label18 = Label(self.khung_giuatren, text = '30k', font = ('Arial Bold', 16), bd = 10)
        self.label18.grid(row = 4, column = 1)

        self.txtcombo18 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo18, bd = 5, state = DISABLED)
        self.txtcombo18.grid(row = 4, column = 2)
        

        self.combo19 = Checkbutton(self.khung_giuatren, text = 'Cheese Ice Cream', variable = self.var19, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo19.grid(row = 5, column = 0, sticky = 'w')
        self.label19 = Label(self.khung_giuatren, text = '20k', font = ('Arial Bold', 16), bd = 10)
        self.label19.grid(row = 5, column = 1)

        self.txtcombo19 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo19, bd = 5, state = DISABLED)
        self.txtcombo19.grid(row = 5, column = 2)
        

        self.combo20 = Checkbutton(self.khung_giuatren, text = 'Caramel', variable = self.var20, onvalue = 1, offvalue = 0,  font = ('arial', 16, 'bold'), command = self.checkbox_giua_bentren)
        self.combo20.grid(row = 6, column = 0, sticky = 'w')
        self.label20 = Label(self.khung_giuatren, text = '20k', font = ('Arial Bold', 16), bd = 10)
        self.label20.grid(row = 6, column = 1)

        self.txtcombo20 = Entry(self.khung_giuatren, font = ('arial', 16, 'bold'), justify = 'center', width = 12, textvariable = self.var_combo20, bd = 5, state = DISABLED)
        self.txtcombo20.grid(row = 6, column = 2)




#-------------XỬ LÍ NÚT ẤN KHUNG GIỮA BÊN DƯỚI---------------
    def exit(self):
        self.delete = messagebox.askyesno('RESTAURANT MANAGEMENT', 'DO YOU WANT TO QUIT?')
        if self.delete == True:
            self.cuaso.destroy()

    def reset(self):
        self.var1.set(0)
        self.var_combo1.set('')
        self.txtcombo1.configure(state = DISABLED)

        self.var2.set(0)
        self.var_combo2.set('')
        self.txtcombo2.configure(state = DISABLED)

        self.var3.set(0)
        self.var_combo3.set('')
        self.txtcombo3.configure(state = DISABLED)

        self.var4.set(0)
        self.var_combo4.set('')
        self.txtcombo4.configure(state = DISABLED)

        self.var5.set(0)
        self.var_combo5.set('')
        self.txtcombo5.configure(state = DISABLED)

        self.var6.set(0)
        self.var_combo6.set('')
        self.txtcombo6.configure(state = DISABLED)

        self.var7.set(0)
        self.var_combo7.set('')
        self.txtcombo7.configure(state = DISABLED)

        self.var8.set(0)
        self.var_combo8.set('')
        self.txtcombo8.configure(state = DISABLED)

        self.var9.set(0)
        self.var_combo9.set('')
        self.txtcombo9.configure(state = DISABLED)

        self.var10.set(0)
        self.var_combo10.set('')
        self.txtcombo10.configure(state = DISABLED)

        self.var11.set(0)
        self.var_combo11.set('')
        self.txtcombo11.configure(state = DISABLED)

        self.var12.set(0)
        self.var_combo12.set('')
        self.txtcombo12.configure(state = DISABLED)

        self.var13.set(0)
        self.var_combo13.set('')
        self.txtcombo13.configure(state = DISABLED)

        self.var14.set(0)
        self.var_combo14.set('')
        self.txtcombo14.configure(state = DISABLED)

        self.var15.set(0)
        self.var_combo15.set('')
        self.txtcombo15.configure(state = DISABLED)

        self.var16.set(0)
        self.var_combo16.set('')
        self.txtcombo16.configure(state = DISABLED)

        self.var17.set(0)
        self.var_combo17.set('')
        self.txtcombo17.configure(state = DISABLED)

        self.var18.set(0)
        self.var_combo18.set('')
        self.txtcombo18.configure(state = DISABLED)

        self.var19.set(0)
        self.var_combo19.set('')
        self.txtcombo19.configure(state = DISABLED)

        self.var20.set(0)
        self.var_combo20.set('')
        self.txtcombo20.configure(state = DISABLED)

        self.tong_tien_hien.configure(text = '')

        




    def tongtien(self):
        try:
            if self.var1.get() == 1:
                t1 = int(self.var_combo1.get())
                
            elif self.var1.get() == 0:
                t1 = int(0)
                

            if self.var2.get() == 1:
                t2 = int(self.var_combo2.get())

            elif self.var2.get() == 0:
                t2 = int(0)
                

            if self.var3.get() == 1:
                t3 = int(self.var_combo3.get())

            elif self.var3.get() == 0:
                t3 = int(0)
                

            if self.var4.get() == 1:
                t4 = int(self.var_combo4.get())

            elif self.var4.get() == 0:
                t4 = int(0)
                

            if self.var5.get() == 1:
                t5 = int(self.var_combo5.get())

            elif self.var5.get() == 0:
                t5 = int(0)
                

            if self.var6.get() == 1:
                t6 = int(self.var_combo6.get())

            elif self.var6.get() == 0:
                t6 = int(0)
                

            if self.var7.get() == 1:
                t7 = int(self.var_combo7.get())

            elif self.var7.get() == 0:
                t7 = int(0)
                

            if self.var8.get() == 1:
                t8 = int(self.var_combo8.get())

            elif self.var8.get() == 0:
                t8 = int(0)
                

            if self.var9.get() == 1:
                t9 = int(self.var_combo9.get())

            elif self.var9.get() == 0:
                t9 = int(0)

            if self.var10.get() == 1:
                t10 = int(self.var_combo10.get())

            elif self.var10.get() == 0:
                t10 = int(0)
                

            if self.var11.get() == 1:
                t11 = int(self.var_combo11.get())

            elif self.var11.get() == 0:
                t11 = int(0)
                

            if self.var12.get() == 1:
                t12 = int(self.var_combo12.get())

            elif self.var12.get() == 0:
                t12 = int(0)
                

            if self.var13.get() == 1:
                t13 = int(self.var_combo13.get())

            elif self.var13.get() == 0:
                t13 = int(0)
                

            if self.var14.get() == 1:
                t14 = int(self.var_combo14.get())

            elif self.var14.get() == 0:
                t14 = int(0)
                

            if self.var15.get() == 1:
                t15 = int(self.var_combo15.get())

            elif self.var15.get() == 0:
                t15 = int(0)
                

            if self.var16.get() == 1:
                t16 = int(self.var_combo16.get())

            elif self.var16.get() == 0:
                t16 = int(0)

            if self.var17.get() == 1:
                t17 = int(self.var_combo17.get())

            elif self.var17.get() == 0:
                t17 = int(0)
                

            if self.var18.get() == 1:
                t18 = int(self.var_combo18.get())

            elif self.var18.get() == 0:
                t18 = int(0)

            if self.var19.get() == 1:
                t19 = int(self.var_combo19.get())

            elif self.var19.get() == 0:
                t19 = int(0)

            if self.var20.get() == 1:
                t20 = int(self.var_combo20.get())

            elif self.var20.get() == 0:
                t20 = int(0)

            #if self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 0\
                #and self.var8.get() == 0 and self.var9.get() == 0 and self.var10.get() == 0 and self.var11.get() == 0 and self.var12.get() == 0 and self.var13.get() == 0 and self.var14.get() == 0\
                 #and self.var15.get() == 0 and self.var16.get() == 0 and self.var17.get() == 0 and self.var18.get() == 0 and self.var19.get() == 0 and self.var20.get() == 0:
                #messagebox.showerror('Error!!!!', 'Mời nhập lại số lượng cần chọn')
                #tong_thanhtoan = ''
                
            
            tong = t1*35000 + t2*55000 + t3*40000 + t4*50000 + t5*40000 + t6*35000 + t7*45000 + t8*35000 + t9*35000 + t10*15000 + t11*15000 + t12*15000 + t13*15000 + t14*10000 + \
                    t15*45000 + t16*30000 + t17*30000 + t18*30000 + t19*20000 + t20*20000
           
            vat = tong/10
            self.tong_thanhtoan = str(tong + vat)
            self.tong_tien_hien = Label(self.khung_giuaduoi, font = ('Arial Bold', 16), width = 19, text = self.tong_thanhtoan, bd = 14, bg = 'red', fg = 'black')
            self.tong_tien_hien.grid(row = 2, column = 1)
            print(self.tong_thanhtoan)

        except:
            messagebox.showerror('Error!!!!', 'Please re-enter the amount')
            


    def Hoadon(self):
        self.hoadon = Toplevel(self.thanhtoan)
        self.hoadon.title('Receipt')
        self.hoadon.geometry('800x600+200+100')


        self.label_hoadon = Label(self.hoadon, text = 'Receipt', font = ('Arial Bold', 20), bd = 6)
        self.label_hoadon.grid(row = 0, column = 1)

        self.thoi_gian_in_hoa_don_print = Label(self.hoadon, text = self.thoi_gian_in_hoa_don, font = ('Arial Bold', 16), bd = 4)
        self.thoi_gian_in_hoa_don_print.grid(row = 1, column = 1)

        self.ten_mon_an = Label(self.hoadon, text = 'Food & Drink', font = ('Arial Bold', 18))
        self.ten_mon_an.grid(row = 3, column = 0)

        self.so_luong_mon_an = Label(self.hoadon, text = 'Amount', font = ('Arial Bold', 18))
        self.so_luong_mon_an.grid(row = 3, column = 1)

        self.tong_tien_mon_an = Label(self.hoadon, text = 'Total amount', font = ('Arial Bold', 18))
        self.tong_tien_mon_an.grid(row = 27, column = 0)

        self.tong_tien_do_an = Label(self.hoadon, text = 'Total', font = ('Arial Bold', 18))
        self.tong_tien_do_an.grid(row = 3, column = 2)

        self.vat_hoa_don = Label(self.hoadon, text = 'Tax', font = ('Arial Bold', 18))
        self.vat_hoa_don.grid(row = 25, column = 0)
        

  

        self.khoang_cach_hoa_don = Label(self.hoadon, text = '     sdsfdsd', font = ('Arial Bold', 25), fg = '#EEEEEE')
        self.khoang_cach_hoa_don.grid(row = 2, column = 0)

        self.khoang_cach_hoa_don_2 = Label(self.hoadon, text = '-', font = ('Arial Bold', 16))
        self.khoang_cach_hoa_don_2.grid(row = 24, column = 0)

        self.khoang_cach_hoa_don_3 = Label(self.hoadon, text = '-', font = ('Arial Bold', 16))
        self.khoang_cach_hoa_don_3.grid(row = 26, column = 0)

        #self.tong_tien_mon_an_ = Label(self.hoadon, text = tong_thanhtoan, font = ('Arial Bold', 16), bd = 4)
        #self.tong_tien_mon_an.grid(row = 27, column = 3)


        if self.var1.get() == 1:
            t1 = int(self.var_combo1.get())
            self.F1 = Label(self.hoadon, text = 'French Fries', font = ('Arial', 16), bd = 4)
            self.F1.grid(row = 4, column = 0)
            self.ff1 = Label(self.hoadon, text = t1, font = ('Arial', 16), bd = 4)
            self.ff1.grid(row = 4, column = 1)

            tongt1 = t1*35000
            self.z1 = Label(self.hoadon, text = tongt1, font = ('Arial', 16), bd = 4)
            self.z1.grid(row = 4, column = 2)

        elif self.var1.get() == 0:
            t1 = 0


        if self.var2.get() == 1:
            t2 = int(self.var_combo2.get())
            if t2 > 0:
                self.F2 = Label(self.hoadon, text = 'Cheeseburger', font = ('Arial', 16), bd = 4)
                self.F2.grid(row = 5, column = 0)
                self.ff2 = Label(self.hoadon, text = t2, font = ('Arial', 16), bd = 4)
                self.ff2.grid(row = 5, column = 1)

                tongt2 = t2*55000
                self.z2 = Label(self.hoadon, text = tongt2, font = ('Arial', 16), bd = 4)
                self.z2.grid(row = 5, column = 2)

        elif self.var2.get() == 0:
            t2 = 0
            

        if self.var3.get() == 1:
            t3 = int(self.var_combo3.get())
            if t3 > 0:
                self.F3 = Label(self.hoadon, text = 'Tacos', font = ('Arial', 16), bd = 4)
                self.F3.grid(row = 6, column = 0)
                self.ff3 = Label(self.hoadon, text = t3, font = ('Arial', 16), bd = 4)
                self.ff3.grid(row = 6, column = 1)

                tongt3 = t3*40000
                self.z3 = Label(self.hoadon, text = tongt3, font = ('Arial', 16), bd = 4)
                self.z3.grid(row = 6, column = 2)

        elif self.var3.get() == 0:
            t3 = 0
                

        if self.var4.get() == 1:
            t4 = int(self.var_combo4.get())
            self.F4 = Label(self.hoadon, text = 'Nachos with extra cheese', font = ('Arial', 16), bd = 4)
            self.F4.grid(row = 7, column = 0)
            self.ff4 = Label(self.hoadon, text = t4, font = ('Arial', 16), bd = 4)
            self.ff4.grid(row = 7, column = 1)

            tongt4 = t4*50000
            self.z4 = Label(self.hoadon, text = tongt4, font = ('Arial', 16), bd = 4)
            self.z4.grid(row = 7, column = 2)

        elif self.var4.get() == 0:
            t4 = 0    

        if self.var5.get() == 1:
            t5 = int(self.var_combo5.get())
            self.F5 = Label(self.hoadon, text = 'Mini burger', font = ('Arial', 16), bd = 4)
            self.F5.grid(row = 8, column = 0)
            self.ff5 = Label(self.hoadon, text = t5, font = ('Arial', 16), bd = 4)
            self.ff5.grid(row = 8, column = 1)

            tongt5 = t5*40000
            self.z5 = Label(self.hoadon, text = tongt5, font = ('Arial', 16), bd = 4)
            self.z5.grid(row = 8, column = 2)

        elif self.var5.get() == 0:
            t5 = 0
            

        if self.var6.get() == 1:
            t6 = int(self.var_combo6.get())
            self.F6 = Label(self.hoadon, text = 'French Toast', font = ('Arial', 16), bd = 4)
            self.F6.grid(row = 9, column = 0)
            self.ff6 = Label(self.hoadon, text = t6, font = ('Arial', 16), bd = 4)
            self.ff6.grid(row = 9, column = 1)

            tongt6 = t6*35000
            self.z6 = Label(self.hoadon, text = tongt6, font = ('Arial', 16), bd = 4)
            self.z6.grid(row = 9, column = 2)

        elif self.var6.get() == 0:
            t6 = 0
            

        if self.var7.get() == 1:
            t7 = int(self.var_combo7.get())
            self.F7 = Label(self.hoadon, text = 'Fire Noodles', font = ('Arial', 16), bd = 4)
            self.F7.grid(row = 10, column = 0)
            self.ff7 = Label(self.hoadon, text = t7, font = ('Arial', 16), bd = 4)
            self.ff7.grid(row = 10, column = 1)

            tongt7 = t7*45000
            self.z7 = Label(self.hoadon, text = tongt7, font = ('Arial', 16), bd = 4)
            self.z7.grid(row = 10, column = 2)

        elif self.var7.get() == 0:
            t7 = 0
            

        if self.var8.get() == 1:
            t8 = int(self.var_combo8.get())
            self.F8 = Label(self.hoadon, text = 'Americano', font = ('Arial', 16), bd = 4)
            self.F8.grid(row = 11, column = 0)
            self.ff8 = Label(self.hoadon, text = t8, font = ('Arial', 16), bd = 4)
            self.ff8.grid(row = 11, column = 1)

            tongt8 = t8*35000
            self.z8 = Label(self.hoadon, text = tongt8, font = ('Arial', 16), bd = 4)
            self.z8.grid(row = 11, column = 2)

        elif self.var8.get() == 0:
            t8 = 0
            

        if self.var9.get() == 1:
            t9 = int(self.var_combo9.get())
            self.F9 = Label(self.hoadon, text = 'Espresso', font = ('Arial', 16), bd = 4)
            self.F9.grid(row = 12, column = 0)
            self.ff9 = Label(self.hoadon, text = t9, font = ('Arial', 16), bd = 4)
            self.ff9.grid(row = 12, column = 1)

            tongt9 = t9*35000
            self.z9 = Label(self.hoadon, text = tongt9, font = ('Arial', 16), bd = 4)
            self.z9.grid(row = 12, column = 2)

        elif self.var9.get() == 0:
            t9 = 0
            

        if self.var10.get() == 1:
            t10 = int(self.var_combo10.get())
            self.F10 = Label(self.hoadon, text = 'Sprite', font = ('Arial', 16), bd = 4)
            self.F10.grid(row = 13, column = 0)
            self.ff10 = Label(self.hoadon, text = t10, font = ('Arial', 16), bd = 4)
            self.ff10.grid(row = 13, column = 1)

            tongt10 = t10*15000
            self.z10 = Label(self.hoadon, text = tongt10, font = ('Arial', 16), bd = 4)
            self.z10.grid(row = 13, column = 2)

        elif self.var10.get() == 0:
            t10 = 0
            

        if self.var11.get() == 1:
            t11 = int(self.var_combo11.get())
            self.F11 = Label(self.hoadon, text = 'Coke', font = ('Arial', 16), bd = 4)
            self.F11.grid(row = 14, column = 0)
            self.ff11 = Label(self.hoadon, text = t11, font = ('Arial', 16), bd = 4)
            self.ff11.grid(row = 14, column = 1)

            tongt11 = t11*15000
            self.z11 = Label(self.hoadon, text = tongt11, font = ('Arial', 16), bd = 4)
            self.z11.grid(row = 14, column = 2)

        elif self.var11.get() == 0:
            t11 = 0
            

        if self.var12.get() == 1:
            t12 = int(self.var_combo12.get())
            self.F12 = Label(self.hoadon, text = 'Juice', font = ('Arial', 16), bd = 4)
            self.F12.grid(row = 15, column = 0)
            self.ff12 = Label(self.hoadon, text = t12, font = ('Arial', 16), bd = 4)
            self.ff12.grid(row = 15, column = 1)
            
            tongt12 = t12*15000
            self.z12 = Label(self.hoadon, text = tongt12, font = ('Arial', 16), bd = 4)
            self.z12.grid(row = 15, column = 2)

        elif self.var12.get() == 0:
            t12 = 0
            

        if self.var13.get() == 1:
            t13 = int(self.var_combo13.get())
            self.F13 = Label(self.hoadon, text = 'Soda', font = ('Arial', 16), bd = 4)
            self.F13.grid(row = 16, column = 0)
            self.ff13 = Label(self.hoadon, text = t13, font = ('Arial', 16), bd = 4)
            self.ff13.grid(row = 16, column = 1)

            tongt13 = t13*15000
            self.z13 = Label(self.hoadon, text = tongt13, font = ('Arial', 16), bd = 4)
            self.z13.grid(row = 16, column = 2)

        elif self.var13.get() == 0:
            t13 = 0
            

        if self.var14.get() == 1:
            t14 = int(self.var_combo14.get())
            self.F14 = Label(self.hoadon, text = 'Water', font = ('Arial', 16), bd = 4)
            self.F14.grid(row = 17, column = 0)
            self.ff14 = Label(self.hoadon, text = t14, font = ('Arial', 16), bd = 4)
            self.ff14.grid(row = 17, column = 1)

            tongt14 = t14*10000
            self.z14 = Label(self.hoadon, text = tongt14, font = ('Arial', 16), bd = 4)
            self.z14.grid(row = 17, column = 2)

        elif self.var14.get() == 0:
            t14 = 0
            

        if self.var15.get() == 1:
            t15 = int(self.var_combo15.get())
            self.F15 = Label(self.hoadon, text = 'Cheesecake', font = ('Arial', 16), bd = 4)
            self.F15.grid(row = 18, column = 0)
            self.ff15 = Label(self.hoadon, text = t15, font = ('Arial', 16), bd = 4)
            self.ff15.grid(row = 18, column = 1)

            tongt15 = t15*45000
            self.z15 = Label(self.hoadon, text = tongt15, font = ('Arial', 16), bd = 4)
            self.z15.grid(row = 18, column = 2)

        elif self.var15.get() == 0:
            t15 = 0
            

        if self.var16.get() == 1:
            t16 = int(self.var_combo16.get())
            self.F16 = Label(self.hoadon, text = 'Creamy Pudding', font = ('Arial', 16), bd = 4)
            self.F16.grid(row = 19, column = 0)
            self.ff16 = Label(self.hoadon, text = t16, font = ('Arial', 16), bd = 4)
            self.ff16.grid(row = 19, column = 1)

            tongt16 = t16*30000
            self.z16 = Label(self.hoadon, text = tongt16, font = ('Arial', 16), bd = 4)
            self.z16.grid(row = 19, column = 2)

        elif self.var16.get() == 0:
            t16 = 0
            

        if self.var17.get() == 1:
            t17 = int(self.var_combo17.get())
            self.F17 = Label(self.hoadon, text = 'Brownies', font = ('Arial', 16), bd = 4)
            self.F17.grid(row = 20, column = 0)
            
            self.ff17 = Label(self.hoadon, text = t17, font = ('Arial', 16), bd = 4)
            self.ff17.grid(row = 20, column = 1)

            tongt17 = t17*25000
            self.z17 = Label(self.hoadon, text = tongt17, font = ('Arial', 16), bd = 4)
            self.z17.grid(row = 20, column = 2)

        elif self.var17.get() == 0:
            t17 = 0
            

        if self.var18.get() == 1:
            t18 = int(self.var_combo18.get())
            self.F18 = Label(self.hoadon, text = 'Tiramisu', font = ('Arial', 16), bd = 4)
            self.F18.grid(row = 21, column = 0)
            self.ff18 = Label(self.hoadon, text = t18, font = ('Arial', 16), bd = 4)
            self.ff18.grid(row = 21, column = 1)

            tongt18 = t18*30000
            self.z18 = Label(self.hoadon, text = tongt18, font = ('Arial', 16), bd = 4)
            self.z18.grid(row = 21, column = 2)

        elif self.var18.get() == 0:
            t18 = 0
            

        if self.var19.get() == 1:
            t19 = int(self.var_combo19.get())
            self.F19 = Label(self.hoadon, text = 'Cheese Ice Cream', font = ('Arial', 16), bd = 4)
            self.F19.grid(row = 22, column = 0)
            self.ff19 = Label(self.hoadon, text = t19, font = ('Arial', 16), bd = 4)
            self.ff19.grid(row = 22, column = 1)

            tongt19 = t19*20000
            self.z19 = Label(self.hoadon, text = tongt19, font = ('Arial', 16), bd = 4)
            self.z19.grid(row = 23, column = 2)

        elif self.var19.get() == 0:
            t19 = 0
            

        if self.var20.get() == 1:
            t20 = int(self.var_combo20.get())
            self.F20 = Label(self.hoadon, text = 'Caramel', font = ('Arial', 16), bd = 4)
            self.F20.grid(row = 23, column = 0)
            self.ff20 = Label(self.hoadon, text = t20, font = ('Arial', 16), bd = 4)
            self.ff20.grid(row = 23, column = 1)

            tongt20 = t20*20000
            self.z20 = Label(self.hoadon, text = tongt20, font = ('Arial', 16), bd = 4)
            self.z20.grid(row = 24, column = 2)

        elif self.var20.get() == 0:
            t20 = 0

        
        tong = t1*35000 + t2*55000 + t3*40000 + t4*50000 + t5*40000 + t6*35000 + t7*45000 + t8*35000 + t9*35000 + t10*15000 + t11*15000 + t12*15000 + t13*15000 + t14*10000 + \
                    t15*45000 + t16*30000 + t17*30000 + t18*30000 + t19*20000 + t20*20000
        
        vat = tong/10
        self.tong_thanhtoan = str(tong + vat)
        
        self.tien_vat_hoa_don =Label(self.hoadon, text = vat, font = ('Arial Bold', 18))
        self.tien_vat_hoa_don.grid(row = 25, column = 2 )

        self.tong_tien_mon_an_hoa_don = Label(self.hoadon, text = self.tong_thanhtoan, font = ('Arial Bold', 16), bd = 4)
        self.tong_tien_mon_an_hoa_don.grid(row = 27, column = 2)


            

            
        '''


        if int(self.var_combo1.get()) >0:
            self.F1 = Label(self.hoadon, text = 'French Fries', font = ('Arial Bold', 14), bd = 4)
            self.F1.grid(row = 4, column = 0)
            self.ff1 = Label(self.hoadon, text = self.var_combo1.get, font = ('Arial Bold', 14), bd = 4)
            self.ff1.grid(row = 4, column = 1)
'''

        
#---------------XỬ LÝ CHECK BOX-----------------
        
         
    #xử lý check box

    def checkbox_trai(self):
        if self.var1.get() == 1:
            self.txtcombo1.configure(state = NORMAL)
            
        elif self.var1.get() == 0:
            self.txtcombo1.configure(state = DISABLED)
            self.var_combo1.set('')

            

        if self.var2.get() == 1:
            self.txtcombo2.configure(state = NORMAL)
            
        elif self.var2.get() == 0:
            self.txtcombo2.configure(state = DISABLED)
            self.var_combo2.set('')

            

        if self.var3.get() == 1:
            self.txtcombo3.configure(state = NORMAL)
            
        elif self.var3.get() == 0:
            self.txtcombo3.configure(state = DISABLED)
            self.var_combo3.set('')
            

        if self.var4.get() == 1:
            self.txtcombo4.configure(state = NORMAL)
            
        elif self.var4.get() == 0:
            self.txtcombo4.configure(state = DISABLED)
            

        if self.var5.get() == 1:
            self.txtcombo5.configure(state = NORMAL)
            
        elif self.var5.get() == 0:
            self.txtcombo5.configure(state = DISABLED)
            self.var_combo5.set('')
            

        if self.var6.get() == 1:
            self.txtcombo6.configure(state = NORMAL)
            
        elif self.var6.get() == 0:
            self.txtcombo6.configure(state = DISABLED)
            self.var_combo6.set('')
            

        if self.var7.get() == 1:
            self.txtcombo7.configure(state = NORMAL)        

        elif self.var7.get() == 0:
            self.txtcombo7.configure(state = DISABLED)
            self.var_combo7.set('')

        
    def checkbox_phai(self):
        if self.var8.get() == 1:
            self.txtcombo8.configure(state = NORMAL)
            
        elif self.var8.get() == 0:
            self.txtcombo8.configure(state = DISABLED)
            self.var_combo8.set('')
            

        if self.var9.get() == 1:
            self.txtcombo9.configure(state = NORMAL)
            
        elif self.var9.get() == 0:
            self.txtcombo9.configure(state = DISABLED)
            self.var_combo9.set('')
            

        if self.var10.get() == 1:
            self.txtcombo10.configure(state = NORMAL)
            
        elif self.var10.get() == 0:
            self.txtcombo10.configure(state = DISABLED)
            self.var_combo10.set('')
            

        if self.var11.get() == 1:
            self.txtcombo11.configure(state = NORMAL)
            
        elif self.var11.get() == 0:
            self.txtcombo11.configure(state = DISABLED)
            self.var_combo11.set('')
            

        if self.var12.get() == 1:
            self.txtcombo12.configure(state = NORMAL)            

        elif self.var12.get() == 0:
            self.txtcombo12.configure(state = DISABLED)
            self.var_combo12.set('')
            

        if self.var13.get() == 1:
            self.txtcombo13.configure(state = NORMAL)

        elif self.var13.get() == 0:
            self.txtcombo13.configure(state = DISABLED)
            self.var_combo13.set('')
            

        if self.var14.get() == 1:
            self.txtcombo14.configure(state = NORMAL)
            
        elif self.var14.get() == 0:
            self.txtcombo14.configure(state = DISABLED)
            self.var_combo14.set('')

    def checkbox_giua_bentren(self):
        if self.var15.get() == 1:
            self.txtcombo15.configure(state = NORMAL)
           
        elif self.var15.get() == 0:
            self.txtcombo15.configure(state = DISABLED)
            self.var_combo15.set('')
            
        if self.var16.get() == 1:
            self.txtcombo16.configure(state = NORMAL)            

        elif self.var16.get() == 0:
            self.txtcombo16.configure(state = DISABLED)
            self.var_combo16.set('')

            
        if self.var17.get() == 1:
            self.txtcombo17.configure(state = NORMAL)
            
        elif self.var17.get() == 0:
            self.txtcombo17.configure(state = DISABLED)
            self.var_combo17.set('')
            

        if self.var18.get() == 1:
            self.txtcombo18.configure(state = NORMAL)           

        elif self.var18.get() == 0:
            self.txtcombo18.configure(state = DISABLED)
            self.var_combo18.set('')
            

        if self.var19.get() == 1:
            self.txtcombo19.configure(state = NORMAL)
            
        elif self.var19.get() == 0:
            self.txtcombo19.configure(state = DISABLED)
            self.var_combo19.set('')
            

        if self.var20.get() == 1:
            self.txtcombo20.configure(state = NORMAL)
            
        elif self.var20.get() == 0:
            self.txtcombo20.configure(state = DISABLED)
            self.var_combo20.set('')

        


    

    
    




c = Cuaso()





