---
output: html_document
runtime: shiny
---
    
library(ggplot2)
library(dplyr)
library(plotly)
library(shiny)
library(shinythemes)

df <- read.csv('/home/kenan/Documents/learning/masters/CUNY-SPS-Masters-DS/DATA_608/module3/data/cleaned-cdc-mortality-1999-2010-2.csv')

ui <- fluidPage(
    theme=shinytheme('cyborg'),
    # Application title
    headerPanel('CDC Mortality 1999-2010'),
    column(3, 
    selectInput('year', 'Year', unique(df$Year), selected='2010'),
    selectInput('icd', 'ICD.Chapter', unique(df$ICD.Chapter), selected='Certain infectious and parasitic diseases'),
    selectInput('state', 'State', unique(df$State), selected='NY')),
    
    mainPanel(
        plotlyOutput('plot1'),
        br(),
        plotlyOutput('plot2')
    )
)

# Define server logic required to draw a histogram
server <- function(input, output, session) {

    # Question 1: As a researcher, you frequently compare mortality rates from particular causes across
    # different States. You need a visualization that will let you see (for 2010 only) the crude
    # mortality rate, across all States, from one cause (for example, Neoplasms, which are
    # effectively cancers). Create a visualization that allows you to rank States by crude mortality
    # for each cause of death.
    
    output$plot1 <- renderPlotly({
        
        p1 <- df %>%
            filter(Year == input$year, ICD.Chapter == input$icd) %>%
            group_by(State) %>% 
            summarise(crude_rate=sum(Crude.Rate))
        
        plot_ly(p1, x = ~reorder(State,crude_rate), y = ~crude_rate, type='bar') %>% 
            layout(title='Crude Mortality Rate vs State')
    })

    # Question 2:
    # Often you are asked whether particular States are improving their mortality rates (per cause)
    # faster than, or slower than, the national average. Create a visualization that lets your clients
    # see this for themselves for one cause of death at the time. Keep in mind that the national
    # average should be weighted by the national population.
    
    output$plot2 <- renderPlotly({
        sdf <- df %>% 
            filter(State == input$state, ICD.Chapter == input$icd) %>%
            group_by(Year) %>% 
            summarise(crude_rate=mean(Crude.Rate))
        ndf <- df %>% group_by(Year) %>% summarise(national_avg=mean(Crude.Rate))
        
        p2 <- cbind(sdf, ndf) %>% select(c('Year', 'crude_rate', 'national_avg'))
        fig <- plot_ly(p2, x =~Year, y = ~crude_rate, name=paste0(input$state, 'Average'), type='scatter', mode='lines')
        fig <- fig %>% add_trace(y = ~national_avg, name = 'National Average', mode = 'lines+markers') 
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
