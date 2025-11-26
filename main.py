from ProjectBuilder import Builder, Project

project = Project('Wrong habbits', 'smoking')
builder = Builder()

@project.Page
def Main(this):
    project.AddPng(this, 'png1.png')
    project.AddPng(this, 'png2.png')
    project.AddPng(this, 'png3.png')
    project.AddChapter(this, 'Introduction', 'Smoking is one of the most common harmful habits, with negative consequences. It leads to various diseases and worsens health.')
    project.AddChapter(this, 'Health causes', 'Smoking causes lung diseases such as bronchitis and lung cancer. It increases the risk of heart disease and stroke. Cigarettes contain substances that cause addiction, making it difficult to quit. Smoking worsens the condition of the skin, making it old and pale. Inflammation in the respiratory pathways caused by smoking can lead to respiratory illnesses. It can also result in death.')
    project.AddChapter(this, 'Consist', 'The main component of cigarettes is tobacco. Tar is added to them for flavor. They contain nicotine, which causes addiction. The composition includes carbon monoxide. Flavorings are often present.Preservatives, such as humectants, are added. The smoke contains formaldehyde. Metals such as cadmium and lead are included. The paper that the tobacco is wrapped in also burns. The filter is made of acetate fiber.')
    project.AddChapter(this, 'End', 'In conclusion, smoking is a dangerous habit that negatively impacts health and quality of life. Quitting smoking helps to prevent many serious diseases.')
    
@builder.Generation
def index():
    [Main]

    builder.AddFont('Schoolbook', 'Schoolbook.ttf')
    builder.AddFont('Amrus', 'amrys.oft')

    builder.SetCss('#label', 'backgroundColor', 'smokewhite')
    builder.SetCss('#sublabel', 'backgroundColor', 'black')

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