from django.contrib import admin
from .models import Order, Device, Customer, DeviceInUse


class DeviceAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'manufacturer', 'model')
    # поля для поиска
    search_fields = ('manufacturer', 'model') 


class OrderAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблиц
    def my_customer(self, obj):
        return obj.customer.customer_name

    def my_serial_number(self, obj):
        return obj.device.serial_number

    def my_device_model(self, obj):
        return obj.device.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.device.analyzer.manufacturer

    # задаём отображаемое название полей в админке
    my_customer.short_description = 'Пользователь'
    my_serial_number.short_description = 'Серийный номер'
    my_device_model.short_description = 'Модель'
    my_device_manufacturer.short_description = 'Производитель'

    # поля для отображения
    list_display = ('id', 'my_device_manufacturer', 'my_device_model', 'my_serial_number',
                    'my_customer', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')
    # поля для поиска
    search_fields = ('customer__customer_name', 'device__id', 'device__serial_number',
                     'device__analyzer__model', 'device__analyzer__manufacturer')
    
    # заменить выпадашку на ввод информации
    raw_id_fields = ('device', )

class CustomerAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')
    # поля для поиска
    search_fields = ('customer_name', 'customer_address')


class DeviceInUseAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблиц
    def my_customer(self, obj):
        return obj.customer.customer_name

    def my_device_model(self, obj):
        return obj.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.analyzer.manufacturer

    # задаём отображаемое название полей в админке
    my_customer.short_description = 'Пользователь'
    my_device_manufacturer.short_description = 'Производитель'
    my_device_model.short_description = 'Модель'

    # поля для отображения
    list_display = ('id', 'my_device_manufacturer', 'my_device_model', 'serial_number', 'my_customer', 'owner_status')

    # поля для поиска
    search_fields = ('serial_number', 'analyzer__manufacturer', 'analyzer__model')
    
    # заменить выпадашку на ввод информации
    raw_id_fields = ('customer', 'analyzer')

admin.site.register(Order, OrderAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInUse, DeviceInUseAdmin)