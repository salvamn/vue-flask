<template>




    <section id="contenedor_conjunto">

        <div id="contenido">


            <div id="contenido_izquierdo">
                <h1>Login</h1>
            </div>

            <div id="contenido_medio">
                <div id="linea">
                </div>
            </div>

            <div id="contenido_derecho">


                <form @submit.prevent="crearUsuario" action="POST">

                    <div id="contenedor_label_input">   
                
                        <input type="text" v-model="nombre_usuario" nombre="nombre_usuario" placeholder="Ingresa tu nombre de usuario">
  
                        <div v-if="v$?.nombre_usuario?.$error && nombre_usuario.length === 0">Ingresa tu nombre de usuario</div>
 
                        <div v-if="v$?.nombre_usuario?.minLength.$error && nombre_usuario.length > 0"> el campo debe contener al menos 4 caracteres</div>
                      
                    </div>
                    
                    <div id="contenedor_label_input">   
            
                        <input type="text" v-model="contrasenia" nombre="contrasenia" placeholder="Ingresa tu contraseña">

                        <div v-if="v$?.contrasenia?.$error">Ingresa tu contraseña</div>

                        <div v-if="v$?.contrasenia?.minLength && contrasenia.length > 0">  el campo debe contener al menos 2 caracteres </div>
                    </div>
                    
                    <div id="contenedor_boton">
                        <button type="submit" @click="validar">Inicia Sesion</button>
                    </div>
                  
                </form>

            </div>

        </div>

    </section>




</template>










<script>

import { useVuelidate } from '@vuelidate/core'
import { required,minLength} from '@vuelidate/validators';
import { useStore } from 'vuex';


import axios from 'axios'

export default {
  components:{

  },
  setup(){

    return { v$: useVuelidate(), store: useStore() }
    
  },
  data() {
    return {
      nombre_usuario: '',
      contrasenia: ''
    };
  },
  methods: {

    validar() {
      this.v$.$touch()
      if (!this.v$.$error) {
        this.login();
        console.log('formulario a sido enviado')
      }else{
        console.log('formulario con errores')
      }

    },





    async login() {
      try {
        const respuesta = await axios.post('http://localhost:5000/login', { 
          nombre_usuario: this.nombre_usuario,
          contrasenia: this.contrasenia
          });


          console.log(respuesta.data)

         if (respuesta.data) {

           this.$store.commit('establecerAutenticado', true); 
           this.$router.push('/panel');
           console.log('autenticacion exitoso');


         } else {
          console.log('autenticacion fallado');
        }

      } catch (error) {
        console.error(error);
      }
    },

  },
  validations: {
      nombre_usuario: {
        required,
        minLength: minLength(6)
      },
      contrasenia: {
        required,
        minLength: minLength(9)
      },

}
}
</script>












<style scoped>
@import url('@/assets/css/formulario.css');
</style>

