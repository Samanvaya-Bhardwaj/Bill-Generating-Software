from tkinter import*
import math, random, os
from tkinter import messagebox
from tkinter import font
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1360x800+0+0')
        self.root.title('Bill Here')
        bg_color="#024535"
        title=Label(self.root,text="Hamara Dhaba Bill",bd=12,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        # ==================Defining of Variable here==================#
# starters variable
        self.pav=IntVar()
        self.tikki=IntVar()
        self.wada=IntVar()
        self.tikka=IntVar()
        self.momo=IntVar()
        self.burgur=IntVar()

        # main course variable
        self.dal=IntVar()
        self.chhole=IntVar()
        self.paneer=IntVar()
        self.naan=IntVar()
        self.roti=IntVar()
        self.tandoor=IntVar()

        # desert variable declaration
        self.rasmalai=IntVar()
        self.gulab=IntVar()
        self.bhari=IntVar()
        self.laddo=IntVar()
        self.imarti=IntVar()
        self.halwa=IntVar()

        # total price wala

        self.total_starter_price=StringVar()
        self.total_main_couse_price=StringVar()
        self.total_desert_price=StringVar()

        self.total_additional_price=StringVar()

        # customer details variables

        self.customername=StringVar()
        self.customerphone=StringVar()

        self.BillNo=StringVar()
        x=random.randint(100,10000)
        self.BillNo.set(str(x))
        self.Search=StringVar()
        
        # additional items variable declaration
        self.additional1=StringVar()
        self.additional3=StringVar()
        self.additional5=StringVar()

        self.additional2=IntVar()
        self.additional4=IntVar()
        self.additional6=IntVar()

#===========customer detail frame===============
        F1=LabelFrame(self.root,text="Customer Details",fg="Brown",bg="orange",font=("times of roman",15,"bold"))
        F1.place(x=0,y=65,relwidth=1)

        customername_lbl=Label(F1,text="Customer Name",bg="Black",fg="white",font=("times new roman",20,"bold")).grid(row=0,column=0,padx=15,pady=2)
        customername_txt=Entry(F1,width=18,textvariable=self.customername,font="italian 15").grid(row=0,column=1,pady=5,padx=10)

        customerphone_lbl=Label(F1,text="Phone No.",bg="black",fg="white",font=("times new roman",20,"bold")).grid(row=0,column=2,padx=15,pady=2)
        customerphone_txt=Entry(F1,width=18,textvariable=self.customerphone,font="italian 15").grid(row=0,column=3,pady=5,padx=10)

        # search_lbl=Label(F1,text="Enter No.",bg="black",fg="white",font=("times new roman",20,"bold")).grid(row=0,column=4,padx=15,pady=2)
        # search_btn=Button(F1,text="Search",command=self.search_phone_no,width=10,font="arial 12 bold",fg="green",bd=3).grid(row=0,column=6, padx=5, pady=5)
        # search_txt=Entry(F1,width=10,font="italian 15").grid(row=0,column=5,pady=5,padx=10)

        # ==================Starter=================#

        F2=LabelFrame(self.root,bd=5,text="Starters(snack)",font=("times new roman",15,"bold"),fg="white",bg=bg_color)
        F2.place(x=5,y=135,width=320,height=340)

# ======================starters entry======================#

        pav_labl=Label(F2,text="Pav Bhaji",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        pav_txt=Entry(F2,width=10,textvariable=self.pav,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=8)

        tikki_labl=Label(F2,text="Aaloo Tikki",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        tikki_txt=Entry(F2,width=10,textvariable=self.tikki, font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        wada_labl=Label(F2,text="Dahi Wada",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        wada_txt=Entry(F2,width=10,textvariable=self.wada,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        tikka_labl=Label(F2,text="Paneer Tikka",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tikka_txt=Entry(F2,width=10,textvariable=self.tikka,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        momo_labl=Label(F2,text="Momos",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        momo_txt=Entry(F2,width=10,textvariable=self.momo,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        burgur_labl=Label(F2,text="Jumbo Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        burger_txt=Entry(F2,width=10,textvariable=self.burgur,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        # =================Main Couse frame================#

        F3=LabelFrame(self.root,bd=5,text="Main Course Items",font=("times new roman",15,"bold"),fg="white",bg=bg_color)
        F3.place(x=325,y=135,width=320,height=340)

        #================= main course item details==================#

        dal_labl=Label(F3,text="Dal Makhni",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        dal_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        chhole_labl=Label(F3,text="Chhole Bhatoore",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        chhole_txt=Entry(F3,width=10,textvariable=self.chhole,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        paneer_labl=Label(F3,text="Sahi Paneer",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        paneer_txt=Entry(F3,width=10,textvariable=self.paneer,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        naan_labl=Label(F3,text="Butter Naan",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        naan_txt=Entry(F3,width=10,textvariable=self.naan,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        roti_labl=Label(F3,text="Tava Roti",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        roti_txt=Entry(F3,width=10,textvariable=self.roti,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        tandoor_labl=Label(F3,text="Tandoori Roti",font=("times new roman",16,"bold"),bg=bg_color,fg="yellow").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        tandoor_txt=Entry(F3,width=10,textvariable=self.tandoor,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        # ======================desert frame===================#
        
        F4=LabelFrame(self.root,bd=5,text="Desert Corner",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=645,y=135,width=290,height=340)

# ======================desert data entry=========================#

        rasmalai_labl=Label(F4,text="Ras-Malai",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rasmalai_txt=Entry(F4,width=10,textvariable=self.rasmalai,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        gulab_labl=Label(F4,text="Gulab Jamun",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        gulab_txt=Entry(F4,width=10,textvariable=self.gulab,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        bhari_labl=Label(F4,text="Ras-Bhari",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        bhari_txt=Entry(F4,width=10,textvariable=self.bhari,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        laddo_labl=Label(F4,text="Laddoo",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        laddo_txt=Entry(F4,width=10,textvariable=self.laddo,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        imarti_labl=Label(F4,text="Imarti",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        imarti_txt=Entry(F4,width=10,textvariable=self.imarti,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        halwa_labl=Label(F4,text="Gajar Halwa",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        halwa_txt=Entry(F4,width=10,textvariable=self.halwa,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ===================bill area frame====================#

        F5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Area",font=("times new roman",15,"bold"),fg="red",bg="white")
        F5.place(x=940,width=330,height=360)

# ==================Bill Label=================#

        bill_title=Label(F5,text="Bill",font="roman 14 bold", bd=5,relief=GROOVE).pack(fill=X)
# =====================Scroll bar and text input in bill area====================#
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # ============buttons frame===============#


        F6=LabelFrame(self.root,bd=5,text="Bill Total",font=("times new roman",15,"bold"),fg="red",bg="sky blue")
        F6.place(x=0,y=475,width=640,height=170)

        # =========details================#

        d1_lbl=Label(F6,text="Total Starter Price",bg="white",fg="red",font=("times new roman,",14,"bold")).grid(row=0,column=0,padx=12,pady=5,sticky="w")
        d1_txt=Entry(F6,width=20,textvariable=self.total_starter_price,font="arial 10 bold",bd=10,relief=SUNKEN).grid(row=0,column=1,padx=12,pady=5)

        d2_lbl=Label(F6,text="Main Course Total",bg="white",fg="red",font=("times new roman,",14,"bold")).grid(row=1,column=0,padx=12,pady=5,sticky="w")
        d2_txt=Entry(F6,width=20,textvariable=self.total_main_couse_price,font="arial 10 bold",bd=10,relief=SUNKEN).grid(row=1,column=1,padx=12,pady=5)

        d3_lbl=Label(F6,text="Total Desert Price",bg="white",fg="red",font=("times new roman,",14,"bold")).grid(row=2,column=0,padx=12,pady=5,sticky="w")
        d3_txt=Entry(F6,width=20,textvariable=self.total_desert_price,font="arial 10 bold",bd=10,relief=SUNKEN).grid(row=2,column=1,padx=12,pady=5)

# ===================total button frame====================#

        btn_F=Frame(F6,bd=5,relief=GROOVE)
        btn_F.place(x=390,y=20,width=200,height=100)

        tot_btn=Button(btn_F,command=self.total,text="Total",bg="light green",fg="red",pady=10,width=22,height=3).grid(row=0,column=0,padx=8,pady=8)

        # ==============bill Generation and clear button(frame and button)=============#

        F7=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Buttons",font=("times new roman",15,"bold"),fg="Brown",bg="grey")
        F7.place(x=955,y=360,width=300,height=125)

        btn_F=Frame(F7,bd=5,relief=GROOVE)
        btn_F.place(x=0,width=280,height=95)

        gen_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="light green",fg="red",pady=10,width=15,height=3).grid(row=0,column=0,padx=8,pady=8)

        clr_btn=Button(btn_F,text="Clear",command=self.clear,bg="light green",fg="red",pady=10,width=15,height=3).grid(row=0,column=1,padx=8,pady=8)
        self.bill_here()

    def total(self):
            self.s_p_p=(self.pav.get()*50)
            self.s_t_p=(self.tikki.get()*40)
            self.s_w_p=(self.wada.get()*30)
            self.s_tikka_p=(self.tikka.get()*70)
            self.s_m_p=(self.momo.get()*30)
            self.s_b_p=(self.burgur.get()*30)

            self.total_starters_price=float(
                    self.s_p_p+
                    self.s_t_p+
                    self.s_w_p+
                    self.s_tikka_p+
                    self.s_m_p+
                    self.s_b_p
            )
            self.total_starter_price.set(str(self.total_starters_price))


            self.mc_d_p=(self.dal.get()*120)
            self.mc_chh_p=(self.chhole.get()*60)
            self.mc_pan_p=(self.paneer.get()*140)
            self.mc_naa_p=(self.naan.get()*15)
            self.mc_rot_p=(self.roti.get()*10)
            self.mc_tand_p=(self.tandoor.get()*20)

            self.total_maincourse_price=float(
                    self.mc_d_p+
                    self.mc_chh_p+
                    self.mc_pan_p+
                    self.mc_naa_p+
                    self.mc_rot_p+
                    self.mc_tand_p
            )
            self.total_main_couse_price.set(str(self.total_maincourse_price))


            self.d_ras_p=(self.rasmalai.get()*30)
            self.d_gul_p=(self.gulab.get()*15)
            self.d_bhar_p=(self.bhari.get()*30)
            self.d_lad_p=(self.laddo.get()*20)
            self.d_imt_p=(self.imarti.get()*20)
            self.d_hlw_p=(self.halwa.get()*40)

            self.total_deserts_price=float(
                    self.d_ras_p+
                    self.d_gul_p+
                    self.d_bhar_p+
                    self.d_lad_p+
                    self.d_imt_p+
                    self.d_hlw_p
            )
            self.total_desert_price.set(str(self.total_deserts_price))
# ========================Assigning totals=========================
            self.Total_Bill=float(self.total_starters_price+
                                  self.total_maincourse_price+
                                  self.total_deserts_price)                 

    def bill_here(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tWelcome To Hamara Dhaba\n")
            self.txtarea.insert(END,f"\nBill No: {self.BillNo.get()}")
            self.txtarea.insert(END,f"\nCustomer Name: {self.customername.get()}")
            self.txtarea.insert(END,f"\nPhone No: {self.customerphone.get()}")
            self.txtarea.insert(END,"\n************************************")
            self.txtarea.insert(END,"Item Name\t\t   QTY\t    Price")
            self.txtarea.insert(END,"\n************************************")

# ============================Bill Output==================

    def bill_area(self):
        if self.customername.get()=="" or self.customerphone.get()=="":
            messagebox.showerror("Error","Name and Phone Number Required")
        else:    
            self.bill_here()
        #     ===================Starters Bill Output=======================
            if self.pav.get()!=0:
                    self.txtarea.insert(END,f"\n Pav Bhaji\t\t   {self.pav.get()}\t    {self.s_p_p}")
            if self.tikki.get()!=0:
                    self.txtarea.insert(END,f"\n Aaloo Tikki\t\t   {self.tikki.get()}\t    {self.s_t_p}")
            if self.wada.get()!=0:
                    self.txtarea.insert(END,f"\n Dahi-Vada\t\t   {self.wada.get()}\t    {self.s_w_p}")
            if self.tikka.get()!=0:
                    self.txtarea.insert(END,f"\n Paneer Tikka\t\t   {self.tikka.get()}\t    {self.s_tikka_p}")
            if self.momo.get()!=0:
                    self.txtarea.insert(END,f"\n Momos\t\t   {self.momo.get()}\t    {self.s_m_p}")
            if self.burgur.get()!=0:
                    self.txtarea.insert(END,f"\n Jumbo Burger\t\t   {self.burgur.get()}\t    {self.s_b_p}")    

#=======================Main Course Bill Output=======================
             
            if self.dal.get()!=0:
                    self.txtarea.insert(END,f"\n Dal Makhni\t\t   {self.dal.get()}\t    {self.mc_d_p}")
            if self.chhole.get()!=0:
                    self.txtarea.insert(END,f"\n Chhole Bhatoore\t\t {self.chhole.get()}\t    {self.mc_chh_p}")
            if self.paneer.get()!=0:
                    self.txtarea.insert(END,f"\n Sahi Paneer\t\t   {self.paneer.get()}\t    {self.mc_pan_p}")
            if self.naan.get()!=0:
                    self.txtarea.insert(END,f"\n Butter Naan\t\t   {self.naan.get()}\t    {self.mc_naa_p}")
            if self.roti.get()!=0:
                    self.txtarea.insert(END,f"\n Tava Roti\t\t   {self.roti.get()}\t    {self.mc_rot_p}")
            if self.tandoor.get()!=0:
                    self.txtarea.insert(END,f"\n Tandoori Naan\t\t   {self.tandoor.get()}\t    {self.mc_tand_p}") 

#========================desert bill output=======================

            if self.rasmalai.get()!=0:
                    self.txtarea.insert(END,f"\n Rasmalai\t\t   {self.rasmalai.get()}\t    {self.d_ras_p}")
            if self.gulab.get()!=0:
                    self.txtarea.insert(END,f"\n Gulab Jamun\t\t   {self.gulab.get()}\t    {self.d_gul_p}")
            if self.bhari.get()!=0:
                    self.txtarea.insert(END,f"\n Ras Bhari\t\t   {self.bhari.get()}\t    {self.d_ras_p}")
            if self.laddo.get()!=0:
                    self.txtarea.insert(END,f"\n Special Laddoo\t\t   {self.laddo.get()}\t    {self.d_lad_p}")
            if self.imarti.get()!=0:
                    self.txtarea.insert(END,f"\n Imarti\t\t   {self.imarti.get()}\t    {self.d_imt_p}")
            if self.halwa.get()!=0:
                    self.txtarea.insert(END,f"\n Gajar Halwa\t\t   {self.halwa.get()}\t    {self.d_hlw_p}")

            self.txtarea.insert(END,f"\n====================================")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t  Rs. {self.Total_Bill}")   
            self.txtarea.insert(END,f"\n====================================") 
            self.save_bill()

# =================backend work=================
    def save_bill(self): 
        op=messagebox.askyesno("Save","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("saved bills/"+str(self.customerphone.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Bill Saved Successfully")
        else: return 

        # search bill using phone no saved        


    def clear(self):
            # starters variable
        self.pav.set(0)
        self.tikki.set(0)
        self.wada.set(0)
        self.tikka.set(0)
        self.momo.set(0)
        self.burgur.set(0)

        # main course variable
        self.dal.set(0)
        self.chhole.set(0)
        self.paneer.set(0)
        self.naan.set(0)
        self.roti.set(0)
        self.tandoor.set(0)

        # desert variable declaration
        self.rasmalai.set(0)
        self.gulab.set(0)
        self.bhari.set(0)
        self.laddo.set(0)
        self.imarti.set(0)
        self.halwa.set(0)

        # total price wala

        self.total_starter_price.set("")
        self.total_main_couse_price.set("")
        self.total_desert_price.set("")

        # customer details variables

        self.customername.set("")
        self.customerphone.set("") 
        self.bill_here()   

root=Tk()
obj = Bill_App(root)
root.mainloop()        