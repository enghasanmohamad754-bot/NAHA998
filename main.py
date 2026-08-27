import os
import requests
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.button import MDFillRoundIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

# حماية الواجهة وعرضها بأبعاد الجوال
Window.size = (360, 640)

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: 0.95, 0.95, 0.96, 1

    MDTopAppBar:
        title: "EngHasan998 | المكتبة الرقمية"
        elevation: 4
        pos_hint: {"top": 1}
        md_bg_color: 0.12, 0.23, 0.37, 1
        right_action_items: [["shield-check", lambda x: app.show_copyright_info()]]

    MDBoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"

        MDLabel:
            text: "مكتبة هندسة النفط والجيولوجيا والصناعات الكيميائية"
            font_style: "Subtitle1"
            bold: True
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0.12, 0.23, 0.37, 1

        MDLabel:
            text: "جميع الحقوق محفوظة © EngHasan998 - مراجع معتمدة ومجانية"
            font_style: "Caption"
            halign: "center"
            theme_text_color: "Hint"

        ScrollView:
            MDList:
                id: books_list

    MDBottomAppBar:
        MDTopAppBar:
            icon: "information"
            type: "bottom"
            mode: "end"
            on_action_button: app.show_copyright_info()
'''

class PetroLibraryApp(MDApp):
    # رابط JSON الخارجي لقائمة الكتب (يُعدله EngHasan998 فقط لإضافة المراجع)
    BOOKS_DATABASE_URL = "https://raw.githubusercontent.com/enghasanmohamad55-spec/NANA99/main/books.json"

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        self.load_books_catalog()

    def load_books_catalog(self):
        """جلب قائمة المراجع بأمان دون إمكانية التعديل من المستخدمين"""
        try:
            response = requests.get(self.BOOKS_DATABASE_URL, timeout=10)
            if response.status_code == 200:
                books = response.json()
                self.populate_list(books)
            else:
                self.show_default_books()
        except Exception:
            self.show_default_books()

    def show_default_books(self):
        """مراجع افتراضية مبدئية عند عدم توفر اتصال بالإنترنت"""
        default_books = [
            {"title": "مبادئ هندسة مكامن النفط", "category": "هندسة النفط", "url": "https://example.com/petroleum.pdf"},
            {"title": "الجيولوجيا التركيبية والاستكشاف", "category": "الجيولوجيا", "url": "https://example.com/geology.pdf"},
            {"title": "أساسيات الصناعات الكيميائية", "category": "الصناعات الكيميائية", "url": "https://example.com/chem.pdf"}
        ]
        self.populate_list(default_books)

    def populate_list(self, books):
        list_widget = self.root.ids.books_list
        list_widget.clear_widgets()

        for book in books:
            item = TwoLineAvatarIconListItem(
                text=book["title"],
                secondary_text=f"التخصص: {book['category']}"
            )
            
            # أيقونة التخصص
            icon = IconLeftWidget(icon="book-open-page-variant")
            item.add_widget(icon)

            # زر التنزيل الآمن
            download_btn = IconRightWidget(
                icon="download",
                on_release=lambda x, b=book: self.download_reference(b)
            )
            item.add_widget(download_btn)
            list_widget.add_widget(item)

    def download_reference(self, book):
        """تنزيل مرجع إلى المجلد المحفوظ بالجوال"""
        try:
            Snackbar(text=f"جاري تنزيل: {book['title']}...").open()
            # يتم إضافة منطق حفظ الملف المباشر هنا
        except Exception as e:
            Snackbar(text="حدث خطأ أثناء التنزيل").open()

    def show_copyright_info(self):
        """نافذة حقوق النشر والحماية"""
        dialog = MDDialog(
            title="علامة تجارية وحقوق محفوظة",
            text="جميع المراجع والمحتويات مملوكة ومصنّفة بواسطة EngHasan998.\n\n"
                 "التطبيق مجاني بالكامل وغير قابل للتعديل أو التخريب من قبل الأطراف الخارجية.",
            buttons=[]
        )
        dialog.open()

if __name__ == '__main__':
    PetroLibraryApp().run()
