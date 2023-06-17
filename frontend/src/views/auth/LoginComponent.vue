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
                        <!--<label for="email">Nombre Usuario</label>-->
                        <input type="text" v-model="nombre_usuario" id="email" placeholder="Ingresa tu nombre de usuario">
                    </div>
                    
                    <div id="contenedor_label_input">   
                        <!--<label for="email">Contraseña</label>--->
                        <input type="text" v-model="contrasenia" id="email" placeholder="Ingresa tu contraseña">
                    </div>
                    
                    <div id="contenedor_boton">
                        <button type="submit">Inicia Sesion</button>
                    </div>
                  
                </form>

            </div>

        </div>

    </section>




</template>




<script>
import { mapState, mapMutations } from 'vuex';
import axios from 'axios'

export default {
  data() {
    return {
      nombre_usuario: '',
      contrasenia: ''
    };
  },
  methods: {
    ...mapMutations(['establecerUsuarioConectado']), 
    async login() {
      try {
        const respuesta = await axios.post('', { nombre_usuario: this.nombre_usuario, contrasenia: this.contrasenia });

         if (respuesta.data.authenticated) {
           this.establecerUsuarioConectado(true); 
           this.$router.push('/panel');
         } else {
          console.log('autenticacion fallado');
        }

      } catch (error) {
        console.error(error);
      }
    },
  },
  computed: {
    ...mapState(['UsuarioConectado']),
  },
};
</script>

<style scoped>
@import url('@/assets/css/formulario.css');
</style>




<style scoped>
@import url('@/assets/css/formulario.css');
</style>