function Mover(obj)
    {
        obj.style.background = "#ffff99";
    }

function MoverFuera(obj)
    {
        obj.style.background = "white";
    }

function CambiaColor(a)
    {
        a.style.background = "#ffff99";
    }
   
//=========================================================================================================
//===================================================JOBS==================================================
//=========================================================================================================

$(document).ready(function()
        {
            $("#otro-menu").click(function(){

                $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
                    function(data){
                        
                        $.each(data.categories,function(i,item){
                            $("#categorias").append("<tr><td>"+item.idCategory+"</td><td>"+item.strCategory +
                            "</td><td><img src='"+ item.strCategoryThumb+"'>"+"</td></tr>");
                            

                        });

                    });
            });
        })

//=========================================================================================================
//=================================================REGISTRO================================================
//=========================================================================================================

$(function() 
      {
        $("#form-reg").validate({
            rules: {
                    rut: "required",
                    dv: "required",
                    name: "required",
                    ap: "required",
                    fecha: "required",
                    phone: "required",
                    email: {
                        required: true,
                        email: true
                    },
                    user: "required",
                    password: "required",
                    password2: {
                        required: true,
                        equalTo: "#password"
                    }   
                    
            }, //rules
            messages: {
                rut: {
                    required: 'Ingresa tu rut',
                },
                dv: {
                    required: 'Ingresa d??gito verificador',
                },
                name: {
                    required: 'Ingresa tu nombre',
                },
                ap: {
                    required: 'Ingresa tu apellido',
                },
                fecha:{
                    required: 'Seleccione una fecha v??lida',
                    min: 'Fecha no corresponde'
                },
                phone:{
                    required: 'Ingrese un n??mero de celular',
                    minlength: 'Cantidad de digitos insuficiente'
                },
                email: {
                    required: 'Ingresa tu correo electr??nico',
                    email: 'Formato de correo no v??lido'
                },
                user: {
                    required: 'Ingresa un nombre de usuario',
                },
                password: {
                    required: 'Ingresa una contrase??a',
                    minlength: 'Caracteres insuficientes'
                },
                password2: {
                    required: 'Repite la contrase??a',
                    equalTo: 'Las contrase??as ingresadas no coinciden',
                    minlength: 'Caracteres insuficientes'

                }
            }//messages
        }); //$('formulario').validate
    }); //function

//=========================================================================================================
//==================================================INICIO=================================================
//=========================================================================================================

$(function() 
      {
        $("#form-log").validate({
            rules: {
                    user: "required",
                    password: "required"
            }, //rules
            messages: {
                user: {
                    required: 'Ingresa un nombre de usuario',
                },
                password: {
                    required: 'Ingresa una contrase??a',
                    minlength: 'Caracteres insuficientes'
                }
            }//messages
        }); //$('formulario').validate
    }); //function

//=========================================================================================================
//=================================================COTIZAR=================================================
//=========================================================================================================

$(function() 
      {
        $("#form-quote").validate({
            rules: {
                name: "required",
                ap: "required",
                evento: "required",
                event: "required",
                servicio: "required",
                menu: "required",
                cant: "required",
                lugar: "required",
                email: {
                    required: true,
                    email: true
                }
            }, //rules
            messages: {
                name: {
                    required: 'Ingresa tu nombre'
                },
                ap: {
                    required: 'Ingresa tu apellido'
                },
                evento: {
                    required: 'Seleccione un tipo de evento'
                },
                event: {
                    required: 'Ingrese una fecha'
                },
                servicio: {
                    required: 'Seleccione un tipo de servicio'
                },
                menu: {
                    required: 'Seleccione un tipo de men??'
                },
                cant: {
                    required: 'Ingresa cantidad de personas'
                },
                lugar: {
                    required: 'Ingresa un lugar'
                },
                email: {
                    required: 'Ingresa tu correo electr??nico',
                    email: 'Formato de correo no v??lido'
                }
            }//messages
        }); //$('formulario').validate
    }); //function