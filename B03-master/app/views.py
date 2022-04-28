from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/world_news/')
    def global_news(self):
        param1 = 'World News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/political_news/')
    def political_news(self):
        param1 = 'Political News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/economic_news/')
    def economic_news(self):
        param1 = 'Economic News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

    @expose('/Entertainment_news/')
    def entertainment_news(self):
        param1 = 'Entertainment News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

    @expose('/housing_news/')
    def housing_news(self):
        param1 = 'Housing News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

"""

class TechnologyView(ModelView):
    datamodel = SQLAInterface(Technology)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class TechnologyCategoryView(ModelView):
    datamodel = SQLAInterface(TechnologyCategory)
    list_columns = ['id', 'name']
    
class TechnologyPageView(BaseView):
    default_view = 'app'

    @expose('/app/')
    def app(self):
        param1 = 'Apps'
        self.update_redirect()
        return self.render_template('technology.html', param1 = param1)

    @expose('/phone/')
    def phone(self):
        param1 = 'Phone'
        self.update_redirect()
        return self.render_template('technology.html', param1=param1)
        
    @expose('/hardware/')
    def hardware (self):
        param1 = 'Hardware'
        self.update_redirect()
        return self.render_template('technology.html', param1=param1)
        
    @expose('/software/')
    def software(self):
        param1 = 'Software'
        self.update_redirect()
        return self.render_template('technology.html', param1=param1)

    @expose('/telecommunications/')
    def telecommunications(self):
        param1 = 'Telecommunications'
        self.update_redirect()
        return self.render_template('technology.html', param1=param1)

class LifeView(ModelView):
    datamodel = SQLAInterface(Life)
    list_olumns = ['id', 'title', 'content', 'date', 'newsCat_id']

class LifeCategoryView(ModelView):
    datamodel = SQLAInterface(LifeCategory)
    list_columns = ['id', 'name']

class LifePageView(BaseView):
    default_view = 'creative'

    @expose('/creative/')
    def creative(self):
        param1 = 'Creative'
        self.update_redirect()
        return self.render_template('life.html', param1 = param1)

    @expose('/healthy/')
    def healthy(self):
        param1 = 'Healthy'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)
        
    @expose('/diet/')
    def diet(self):
        param1 = 'Diet'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)
        
    @expose('/emotion/')
    def emotion(self):
        param1 = 'Emotion'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)

    @expose('/travel/')
    def travel (self):
        param1 = 'Travel'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)

    @expose('/work/')
    def work(self):
        param1 = 'Work'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)
        
    @expose('/activity/')
    def activity(self):
        param1 = 'Activity'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)

    @expose('/campus/')
    def campus(self):
        param1 = 'Campus'
        self.update_redirect()
        return self.render_template('life.html', param1=param1)

class InterestPageView(BaseView):
    default_view = 'sports'

    @expose('/sports/')
    def sports(self):
        param1 = 'Sports'
        self.update_redirect()
        return self.render_template('interest.html', param1 = param1)

    @expose('/academic/')
    def academic(self):
        param1 = 'Academic'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)
        
    @expose('/story/')
    def story(self):
        param1 = 'Story'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)
        
    @expose('/game/')
    def game(self):
        param1 = 'Game'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/film/')
    def film(self):
        param1 = 'Film'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/cartoon/')
    def cartoon(self):
        param1 = 'Cartoon'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)
    @expose('/photograghy/')
    def photograghy(self):
        param1 = 'Photography'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/music/')
    def music(self):
        param1 = 'Music'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/car/')
    def car(self):
        param1 = 'Car'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/pet/')
    def pet(self):
        param1 = 'Pet'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/trend/')
    def trend(self):
        param1 = 'Trend'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/toys/')
    def toys(self):
        param1 = 'Toys'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)

    @expose('/live/')
    def live(self):
        param1 = 'Live'
        self.update_redirect()
        return self.render_template('interest.html', param1=param1)


class OtherPageView(BaseView):
    default_view = 'chat'

    @expose('/chat/')
    def chat(self):
        param1 = 'Chat'
        self.update_redirect()
        return self.render_template('other.html', param1 = param1)

    @expose('/station_service/')
    def station_service(self):
        param1 = 'Station Service'
        self.update_redirect()
        return self.render_template('other.html', param1=param1)
        
    @expose('/black_hole/')
    def black_hole(self):
        param1 = 'Black Hole'
        self.update_redirect()
        return self.render_template('other.html', param1=param1)
"""

db.create_all()

""" News View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("World", href="/newspageview/World_news/", category="News")
appbuilder.add_link("Political", href="/newspageview/Political_news/", category="News")
appbuilder.add_link("Economic", href="/newspageview/Economic_news/", category="News")
appbuilder.add_link("Entertainment", href="/newspageview/Entertainment_news/", category="News")
appbuilder.add_link("Housing", href="/newspageview/Housing_news/", category="News")

""" Technology View """
"""
appbuilder.add_view(TechnologyPageView, 'Apps', category="Technology")
appbuilder.add_link("App", href="/technologypageview/App/", category="Technology")
appbuilder.add_link("Phone", href="/technologypageview/Phone/", category="Technology ")
appbuilder.add_link("Hardware", href="/technologypageview/Hardware/", category="Technology")
appbuilder.add_link("Software", href="/technologypageview/Software/", category="Technology")
appbuilder.add_link("Telecommunications", href="/technologypageview/Telecommunications/", category="Technology")
"""

#""" Life View """
"""
appbuilder.add_view(LifePageView, 'Creative', category="Life")
appbuilder.add_link("Healthy", href="/lifepageview/Healthy/", category="Life")
appbuilder.add_link("Diet", href="/lifepageview /Diet/", category="Life")
appbuilder.add_link("Emotion", href="/lifepageview /Emotion/", category="Life")
appbuilder.add_link("Travel", href="/lifepageview /Travel/", category="Life")
appbuilder.add_link("Work", href="/lifepageview /Work/", category="Life")
appbuilder.add_link("Activity", href="/lifepageview /Activity/", category="Life")
appbuilder.add_link("Campus", href="/lifepageview /Campus/", category="Life")
"""

# Interest View
"""
appbuilder.add_view(InterestPageView, 'Sports', category="Interest")
appbuilder.add_link("Academi", href="/interestpageview/Academi/", category="Interest")
appbuilder.add_link("Story", href="/interestpageview/Story/", category="Interest")
appbuilder.add_link("Game", href="/interestpageview/Game/", category="Interest")
appbuilder.add_link("Film", href="/interestpageview/Film/", category="Interest")
appbuilder.add_link("Cartoon", href="/interestpageview/Cartoon/", category="Interest")
appbuilder.add_link("Photography", href="/interestpageview/Photography/", category="Interest")
appbuilder.add_link("Music", href="/interestpageview/Music/", category="Interest")
appbuilder.add_link("Car", href="/interestpageview/Car/", category="Interest")
appbuilder.add_link("Pet", href="/interestpageview/Pet/", category="Interest")
appbuilder.add_link("Trend", href="/interestpageview/Trend/", category="Interest")
appbuilder.add_link("Toys", href="/interestpageview/Toys/", category="Interest")
appbuilder.add_link("Live", href="/interestpageview/Live/", category="Interest")
"""

#Other View
"""
appbuilder.add_view(OtherPageView, 'Chat', category="Other")
appbuilder.add_link("Station Service", href="/otherpageview/Station Service/", category="Other")
appbuilder.add_link("Black Hole", href="/otherpageview/Black Hole/", category="Other")
"""

# Custom Views 
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

