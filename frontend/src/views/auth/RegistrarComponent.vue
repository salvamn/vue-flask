<template>


  
<section id="contenedor_conjunto">

  <div id="contenido">


      <div id="contenido_izquierdo">
          <h1>Registrate</h1>
      </div>

      <div id="contenido_medio">
          <div id="linea">
          </div>
      </div>

      <div id="contenido_derecho">


          <form @submit.prevent="validar" action="POST">
              <div id="contenedor_label_input">   
                  <!--<label for="email">Nombre Usuario</label>-->
                  <input type="text" v-model="nombre" id="email" placeholder="Ingresa tu nombre">

                <div v-if="enviado && !$v.nombre.required"> Debe escribir un nombre </div>
                  
              </div>

              <div id="contenedor_label_input">  
                <input type="text" v-model="correo" id="correo" placeholder="Ingresa tu correo">
              </div>

              <div id="contenedor_label_input">  
                <input type="text" v-model="nombre_usuario" id="nombre_usuario" placeholder="Ingresa tu nombre de usuario">
              </div>

              <div id="contenedor_label_input">   
                 
                  <input type="text" v-model="contrasenia" id="email" placeholder="Ingresa tu contraseña">
              </div>

            
              
              <div id="contenedor_boton">
                  <button type="submit">Registrarme</button>
              </div>
            
          </form>

      </div>

  </div>

</section>






</template>














<script>

import { mapState } from 'vuex';
import { required } from 'vuelidate/lib/validators';



export default {
  components: {
  },
  data() {
    return {
      nombre: '',
      correo: '',
      nombre_usuario: '',
      contrasenia: '',
      enviado: false,
    };
  },
  methods: {
    validar(){
        this.enviado=true;
        if (this.$v.$invalid){
          //console.log('hay campos invalidos en el formulario')
          return;
        }

        this.enviado = this.crearUsuario();
      },

    async crearUsuario() {

      const usuario = {
        nombre: this.nombre,
        correo: this.correo,
        nombre_usuario: this.nombre_usuario,
        contrasenia: this.contrasenia
      };

     

      try {
        const respuesta = await this.$store.dispatch('crearUsuario', usuario);
        console.log(respuesta);

        //this.$router.push('/panel');
      } catch (error) {
        console.error(error);
      }
    }
  },
  validations: {
    nombre:{
      required,
    }

  },
  computed: {
    ...mapState(['usuarios']),
  },
};
</script>

















<style scoped>
@import url('@/assets/css/formulario.css');

</style>