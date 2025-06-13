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

  method lluvia(){
    if(max_hidratacion<=100){
      hidratacion += 10
      return
    }else{
      return
    }
  }
  
  method sol(){
    if(max_energia<=100){
      energia += 10
      return
    }else{
      return
    }
  }
  
  method profesional(tierra){
    tamano = tamano + tierra.profesional() * crecimiento()
  }
  method preparada(tierra){
    tamano = tamano + tierra.preparada() * crecimiento()
  }
  method organica(tierra){
    tamano = tamano + tierra.organica() * crecimiento()
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

class Tierra{
  const tierra = #{"preparada","profesional","organica"}
  const property preparada = tierra.get(0) 
  const property profesional = tierra.get(1)
  const property organica = tierra.get(2)
  
}

object preparada{
  method crecimiento() = 5
}
object profesional{
  method crecimiento() = 8
}
object organica{
  method crecimiento() = 3
}