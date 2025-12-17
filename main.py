from ProjectBuilder import Builder, Project

project = Project('English project', 'Outfit styles')
builder = Builder()

@project.Page
def Main(this):
    project.AddPng(this, 'png1.png')
    project.AddPng(this, 'png2.png')
    project.AddPng(this, 'png3.png')
    project.AddChapter(this, 'Introduction', 'Clothing is an important part of our daily lives. It can help feel comfortable. Different situations require different types of outfits. Here are some examples of everyday, school, and formal clothing.')
    project.AddChapter(this, 'Clothes', 'A casual outfit is perfect for relaxing or hanging out with friends. Usually, it includes jeans, t-shirts, and sneakers. These clothes are comfortable and easy to wear. A school outfit often consists of a uniform. Many schools require students to wear shirts, pants and sometimes ties. It helps to create a discipline. The clothes are simple for learning.A formal outfit usually for special events like ceremonies. It includes dresses, suits, or tuxedos. These clothes often have elegant details and high-quality fabrics. They make the wearer look stylish.')
    project.AddChapter(this, 'Concluse', 'Wearing the right outfit can boost confidence and make a good impression. Everyone should feel comfortable and stylish in their clothes.')
    
@builder.Generation
def index():
    [Main]

    builder.AddFont('Schoolbook', 'Schoolbook.ttf')
    builder.AddFont('Amrus', 'amrys.oft')

    builder.SetCss('#label', 'backgroundColor', 'whitesmoke')
    builder.SetCss('#sublabel', 'backgroundColor', 'yellow')

    builder.SetCss('#sublabel', 'color', 'white')

    builder.SetCss('.chptname', 'fontFamily', 'almys')

    builder.SetCss('.chptdescribe', 'paddingLeft', '15%')
    builder.SetCss('.chptdescribe', 'paddingRight', '15%')
    builder.SetCss('.chptdescribe', 'fontSize', '35px')
    
    builder.SetCss('button', 'fontSize', '350%')
    builder.SetCss('body', 'fontFamily', 'Schoolbook')
    builder.SetCss('button', 'fontFamily', 'almys')
    builder.SetCss('button', 'marginTop', '2%')
    builder.SetCss('button', 'fontSize', '390%')

    builder.SetCss('img', 'padding', '2%')

builder.BuildProject(project, index, start_function='Main')