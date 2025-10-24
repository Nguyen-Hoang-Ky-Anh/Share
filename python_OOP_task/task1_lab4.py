class Monhoc:
    def __init__(self, maSo, ten, soTinchi, loai):
        self.__maSo = maSo
        self.__ten = ten
        self.__soTinChi = soTinchi
        self.__loai = loai
    
    def getMaSo(self):
        return self.__maSo
    
    def getTen(self):
        return self.__ten
    
    def getSoTinChi(self):
        return self.__soTinChi
        
    def getLoai(self):
        return self.__loai
    
    def __str__(self):
        return '[Ma so: ' + self.__maSo + ', ten: ' + self.__ten + ', so tin chi: ' + self.__soTinChi + ', loai: ' + self.__loai +']'
        
class GiangVien:
    def __init__(self, hoTen, namSinh, dsMonHoc = []):
        self.__hoTen = hoTen
        self.__namSinh = namSinh
        self.__dsMonHoc = dsMonHoc
    
    def getHoTen(self):
        return self.__hoTen
    
    def getDsMonHoc(self):
        return self.__dsMonHoc
    
    # 1) Count the courses that a lecturer can teach with a given type    
    def demSoMon(self, loai):
        return len([mh for mh in self.getDsMonHoc() if mh.getLoai() == loai])
    
    # Get total credit that a lecturer teachs
    def demSoTinChi(self):
        return sum([mh.getSoTinChi() for mh in self.getDsMonHoc()])
    
    
        
class Khoa:
    def __init__(self, ten, diaChi, dsgv = []):
        self.__ten = ten
        self.__diaChi = diaChi
        self.__dsgv = dsgv
    
    def getDsgv(self):
        return self.__dsgv
    
    # 2) to find a lecturer who can teach courses with the highest total number of credits. 
    def timGiangVienDayNhieuTinChiNhat(self):
        return max(gv.demSoTinChi for gv in self.getDsgv())
    
    # 3) statisticize courses by type, with key being the type of a course and the value is a list of corresponding courses.
    def thongKeMonHocTheoLoai(self):
        return {loai : [mh for gv in self.getDsgv() 
                        for mh in gv.getDsMonHoc() 
                        if mh.getLoai() == loai]
                for loai in (mh.getLoai() 
                                for gv in self.getDsgv() 
                                for mh in gv.getDsMonHoc())}
        
    # 4) filter courses based on the lecturer’s name and course type. 
    #    The results should be sorted by the name of each course.
    def timMonHoc(self, tenGiangVien, loai):
        dsMhGvDcChiDinh = [mh for gv in self.getDsgv() 
                           if gv.getHoTen() == tenGiangVien 
                           for mh in gv.getDsMonHoc()
                           if mh.getLoai() == loai]
        return sorted(dsMhGvDcChiDinh, key = lambda mh : mh.getTen())

def main():
    # Tạo các môn học
    mh1 = Monhoc("MH01", "Toán", 3, "Tự nhiên")
    mh2 = Monhoc("MH02", "Văn", 2, "Xã hội")
    mh3 = Monhoc("MH03", "Lý", 3, "Tự nhiên")
    mh4 = Monhoc("MH04", "Sử", 2, "Xã hội")
    mh5 = Monhoc("MH05", "Hóa", 3, "Tự nhiên")

    # Tạo giảng viên
    gv1 = GiangVien("Nguyễn Văn A", 1980, [mh1, mh2])
    gv2 = GiangVien("Trần Thị B", 1985, [mh3, mh4, mh5])

    # Tạo khoa
    khoa = Khoa("Khoa Khoa học", "123 Đường ABC", [gv1, gv2])

    # 1. Đếm số môn theo loại của giảng viên
    print("Số môn Tự nhiên của GV1:", gv1.demSoMon("Tự nhiên"))
    print("Số môn Xã hội của GV2:", gv2.demSoMon("Xã hội"))

    # 2. Tổng số tín chỉ của mỗi giảng viên
    print("Tổng số tín chỉ GV1:", gv1.demSoTinChi())
    print("Tổng số tín chỉ GV2:", gv2.demSoTinChi())

    # 3. Giảng viên dạy nhiều tín chỉ nhất
    gv_max = max(khoa.getDsgv(), key=lambda gv: gv.demSoTinChi())
    print("Giảng viên dạy nhiều tín chỉ nhất:", gv_max.getHoTen())

    # 4. Thống kê môn học theo loại
    print("\nThống kê môn học theo loại:")
    thongke = khoa.thongKeMonHocTheoLoai()
    for loai, ds in thongke.items():
        print(f"- Loại: {loai}")
        for mh in ds:
            print(f"  + {mh.getTen()} ({mh.getSoTinChi()} tín chỉ)")

    # 5. Tìm môn học theo tên giảng viên và loại
    print("\nCác môn Tự nhiên của giảng viên Trần Thị B:")
    ds_mon = khoa.timMonHoc("Trần Thị B", "Tự nhiên")
    for mh in ds_mon:
        print(f"- {mh.getTen()} ({mh.getMaSo()})")

if __name__ == "__main__":
    main()
