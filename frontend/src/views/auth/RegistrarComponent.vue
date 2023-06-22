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


        <form @submit.prevent="crearUsuario" action="POST">
          <div id="contenedor_label_input">
            <!--<label for="email">Nombre Usuario</label>-->
            <input type="text" v-model="usuario.nombre" nombre="nombre" placeholder="Ingresa tu nombre" required>

            <div v-if="v$?.usuario.nombre?.$error">Ingresa el nombre porfavor</div>

          </div>

          <div id="contenedor_label_input">
            <input type="text" v-model="usuario.correo" nombre="correo" placeholder="Ingresa tu correo" required>

            <div v-if="v$?.usuario.correo?.$error">hey, no has ingresado el correo, ingresalo denuevo</div>
          </div>

          <div id="contenedor_label_input">
            <input type="text" v-model="usuario.nombre_usuario" nombre="nombre_usuario" placeholder="Ingresa tu nombre de usuario" required>

            <div v-if="v$?.usuario.nombre_usuario?.$error">ingresa el nombre usuario ya que se te olvido</div>
          </div>

          <div id="contenedor_label_input">

            <input type="text" v-model="usuario.contrasenia" nombre="contrasenia" placeholder="Ingresa tu contraseña" required>

            <div v-if="v$?.usuario.contrasenia?.$error">Ingresa la contraseña</div>
          </div>



          <div id="contenedor_boton">
            <button type="submit" @click="validar" >Registrarme</button>
          </div>

        </form>

      </div>

    </div>

  </section>
</template>














<script>

import { mapState } from 'vuex';
import { useVuelidate } from '@vuelidate/core'
import { required,minLength,email } from '@vuelidate/validators';



export default {
  components: {
  },
  setup(){
    return { v$: useVuelidate() }
  },
  data() {
    return {
      usuario: {
        nombre: '',
        correo: '',
        nombre_usuario: '',
        contrasenia: '',
      }
    }
  },
  methods: {

    validar() {
      this.v$.$touch()
      if (!this.v$.$error) {
        console.log('formulario a sido enviado')
      }else{
        console.log('formulario con errores')
      }

    },

    
    async crearUsuario() {
      const usuario = {
        nombre: this.usuario.nombre,
        correo: this.usuario.correo,
        nombre_usuario: this.usuario.nombre_usuario,
        contrasenia: this.usuario.contrasenia
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
    usuario: {
      nombre: {
        required,
      },
      correo: {
        required,
        email,
      },
      nombre_usuario: {
        required,
      },
      contrasenia: {
        required,
        minLength: minLength(5)
      }
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