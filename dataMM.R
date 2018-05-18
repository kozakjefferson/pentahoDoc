install.packages("lubridate")
install.packages("plotly")

install.packages("plyr")
install.packages("RODBC")
library(lubridate)
library(plotly)
df$DataCompra <-  month(as.POSIXlt(df$DataCompra, format="%Y-%m"))
summary(df)
df$DataCompra
planes <- group_by(hflights_df, TailNum)
?aggregate
df %>% group_by(df$DataCompra) %>% filter(df$tipo))
install.packages("dplyr")
library("dplyr") 
filter(df$DataCompra==4)
str(df)
fdf <- filter(dftbl,DataCompra==3)
names(df) <- c("NotaPai","DataCompra","idStatua","Status","tipo","origem","6","pessoaVenda","8","estado","cidade","tipocidade","12","IdCompra","tipoCompra","parcelas","valorSemFrete","desconto","valorFrete","valorPedido","000","naosei","vti","idTipo","tpoVenda","valorUnitario","quantidadeProduto","valorProduto","idlost") 
fdf
str(fdf)
dftbl <- tbl_df(df)
dftbl
dfe <- group_by(dftbl,DataCompra)
dfe
summary(dfe)
s <- summarise(dftbl, sum(valorPedido),sum(desconto))
aggSumMOnth <- aggregate(data=df,log(df$valorPedido+df$valorFrete-df$desconto)~df$DataCompra,sum)
aggSumMOnthdevi <- aggregate(data=df,df$valorPedido+df$valorFrete-df$desconto~df$tpoVenda,sum)
aggSumMOnthdeviData <- aggregate(data=df,list(df$tpoVenda,df$DataCompra), FUN="mean")
aggMeanMOnth <- aggregate(data=df,df$valorPedido+df$valorFrete-df$desconto~df$DataCompra,mean)

head(aggSumMOnth)
head(aggMeanMOnth)
head(aggSumMOnthdevi)
?


str(s)
dftbl$ID <- seq.int(nrow(dftbl))
head(dftbl)
str(dftbl)
plot(dftbl$DataCompra,dftbl$valorPedido)
barplot(dftbl$DataCompra,xlab = dftbl$valorPedido)
boxplot(df$DataCompra, df$valorPedido)
mes <- c("Março","Abril","Maio")
?boxplot
boxplot()
p <- plot_ly(y=df$valorPedido,
        x=df$DataCompra, type = "bar")
z <- plot_ly(z=df$valorPedido, type = "heatmap")
chart_link = api_create(p, filename="bar-basic")
p
chart_link
z

barplot(dftbl$valorPedido,dftbl$DataCompra)




p <- plot_ly(df, x = ~DataCompra, y = ~valorPedido, type = 'bar', name = 'pedido') %>%
  add_trace(y = ~valorFrete, name = 'frete') %>%
  add_trace(y= ~naosei, name= 'naosei') %>%
  layout(yaxis = list(title = 'Count'), barmode = 'stack')

p
cb <- cbind(df$valorFrete,df$valorPedido)
colSums(cb)
head(cb)
sum(cb)
rowsum(cb)
resmodelo <- lm(df$DataCompra~df$valorPedido)
lmy
shapiro.test(rstudent(resmodelo))
plot(rstudent(resmodelo) ~ fitted(resmodelo), pch = 19)
abline(h = 0, lty = 2)
plot(df$DataCompra~df$valorPedido)
abline(resmodelo,lty=2) 
