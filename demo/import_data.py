import os
import django
import csv
from datetime import datetime
from django.utils.timezone import make_aware
from myapp.models import Segment, Customer, Category, Product, Bill, BillLine

# Thiết lập môi trường Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()

file_path = "data_ggsheet.csv"

with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Loại bỏ khoảng trắng và kiểm tra giá trị rỗng
        segment_code = row.get("Mã PKKH", "").strip()
        segment_info = row.get("Mô tả Phân Khúc Khách hàng", "").strip()
        customer_code = row.get("Mã khách hàng", "").strip()
        category_code = row.get("Mã nhóm hàng", "").strip()
        category_name = row.get("Tên nhóm hàng", "").strip()
        product_code = row.get("Mã mặt hàng", "").strip()
        product_name = row.get("Tên mặt hàng", "").strip()
        unit_price_str = row.get("Đơn giá", "0").strip()
        bill_code = row.get("Mã đơn hàng", "").strip()
        time_created_str = row.get("Thời gian tạo đơn", "").strip()
        quantity_str = row.get("SL", "0").strip()
        total_price_str = row.get("Thành tiền", "0").strip()

        # Chuyển đổi kiểu dữ liệu an toàn
        try:
            unit_price = float(unit_price_str) if unit_price_str else 0
            quantity = int(quantity_str) if quantity_str else 0
            total_price = int(total_price_str) if total_price_str else 0
        except ValueError:
            print(f"Lỗi chuyển đổi dữ liệu trong dòng: {row}")
            continue  # Bỏ qua dòng bị lỗi

        # Chuyển đổi datetime
        try:
            time_created_clean = time_created_str.replace("  ", " ")  # Chuẩn hóa khoảng trắng
            time_created = make_aware(datetime.strptime(time_created_clean, "%Y-%m-%d %H:%M:%S"))
        except ValueError:
            print(f"Lỗi datetime: {time_created_str} trong dòng {row}")
            continue  # Bỏ qua dòng bị lỗi

        # Tạo hoặc lấy dữ liệu
        segment, _ = Segment.objects.get_or_create(
            segment_code=segment_code, defaults={"segment_info": segment_info}
        )
        customer, _ = Customer.objects.get_or_create(
            customer_code=customer_code, defaults={"segment": segment}
        )
        category, _ = Category.objects.get_or_create(
            category_code=category_code, defaults={"category_name": category_name}
        )
        product, _ = Product.objects.get_or_create(
            product_code=product_code, defaults={"product_name": product_name, "price": unit_price, "category": category}
        )
        bill, _ = Bill.objects.get_or_create(
            bill_code=bill_code, defaults={"time_created": time_created, "customer": customer}
        )

        # Tạo dòng hóa đơn (BillLine)
        bill_line, _ = BillLine.objects.get_or_create(
            bill=bill,
            product=product,
            defaults={"quantity": quantity, "total_price": total_price}
        )


print("Dữ liệu đã nhập thành công!")
