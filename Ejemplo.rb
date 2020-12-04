require 'date'
#VerificarCodigo
class Ejercicio1
  def fechas
    t = Time.now
    puts "Dia: #{t.day}"
    puts "Mes: #{t.month}"
    puts "Año: #{t.year}"
    puts "Hora: #{t.hour}"
    puts "Minuto: #{t.min}"
    puts "Segundo: #{t.sec}"
    puts "Dia de la semana: #{t.wday}"
    puts "Mes en string: #{t.strftime("%B")}"
    puts "Dia de la semana: #{t.strftime("%A")}"
    puts "Meridiano: #{t.strftime("%p")}"

    vacacion=Time.mktime(2007,"dec",31,1,15,20)   #  "Mon Dec 31 01:15:20 +1000 2007 "
  end

  def fechaDate
    fecha = Date.new(2020,12,04)
    puts "fecha creada: "+fecha.to_s
    hoy = Date.today
    puts "fecha de hoy: "+hoy.to_s

  end
end

fecha = Ejercicio1.new()
fecha.fechas()
puts""
fecha.fechaDate()