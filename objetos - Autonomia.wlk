class Planta{
  var tamano = 0
  var inventario = 0
  var hidratacion = 50
  var energia = 50
  var max_hidratacion = 100
  var max_energia = 100
  
  method existe() = tamano > 0
  
  method cosechar(){
    if (tamano>=25)
    tamano = 0
    inventario += 1
  }
  method energizar(){
  if(energia<=9){
    return
  }else{
  energia -= 10 
  tamano += 3
  return}
}
  
  method hidratar() {
  if(hidratacion<=9){
    return
  }else{
  hidratacion -= 10
  tamano += 3
  return
  }
}
}

object girasol inherits Planta{
  var polen = 15
  method polenizar(){
    tamano = tamano + polen
    polen = 0
  }
  
}

object flor inherits Planta{
  var petalos = 10
  method petalizar(){
    tamano = tamano + petalos
    petalos = 0
  }
  
  
}