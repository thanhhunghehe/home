from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])  # định nghĩa route cho trang chủ
def home():#sẽ gọi hàm home 
    ten = None
    if request.method == 'POST':  # kiểm tra nếu là phương thức POST
        ten = request.form.get('ten')  # lấy giá trị của trường 'ten' từ form
    # nếu không có giá trị
    return render_template ('index.html', ten=ten)#trả về nội dung của file index.html trong thư mục templates
if __name__ == '__main__':
    app.run(debug=True)#giúp dễ kiểm tra lỗi khi chạy ứng dụng