<template>



    <nav id="navSito">


        <div id="contenedor_autenticado" v-if="estaAutenticado">

            <div id="contenedor_logo_autenticado">
                <router-link style="text-decoration: none;" to="/panel">Mis paneles</router-link>
            </div>

            <div id="submenu">
                <strong>{{ nombreUsuario }}</strong>
                <div id="submenu-contenido">
                    <router-link style="text-decoration: none;" to="/panel">Panel</router-link>
                    <router-link to="/" @click.prevent="cerrarSesion">Cerrar sesión</router-link>
                </div>
            </div>


        </div>



        <div id="contenedor_noautenticado" v-else>

            <div id="contenedor_logo">
                <img src="@/assets/img/icons/codigo.png" alt="">
            </div>

            <div id="contenedor_rutas">
                <router-link id="rutas" to="/Inicio" title="iniciar sesion">Inicio</router-link>
                <router-link id="rutas" to="/login" title="iniciar sesion">Iniciar Sesión</router-link>
                <router-link id="rutas" to="/registrar" title="registrarse">¿No tienes una cuenta?</router-link>
            </div>


        </div>


    </nav>



</template>





<script>
import { mapState } from 'vuex';
export default {
    data() {
        return {
            usuarioAutenticado: null
        }
    },
    computed: {
        ...mapState(['estaAutenticado', 'nombreUsuario']),
    },
    methods: {

        cerrarSesion() {
            this.$store.commit('establecerAutenticado', false);
            this.$store.commit('establecerNombreUsuario', '');
            this.$router.push('/login');

        }
    }
}



</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */

   #navSito {
       width: 100%;
       background-color: rgb(5, 5, 5);
       display: flex;
       justify-content: space-around;
       align-items: center;
       padding: 5px;
       position: fixed;
       top: 0;
   }

   #navSito #contenedor_logo {
       color: white;
       font-size: 30px;
   }

   #navSito #contenedor_logo img {
       width: 1.5em;
       filter: invert(100%);
   }

   #navSito #contenedor_rutas {
       display: flex;
       gap: 40px;

   }

   #contenedor_autenticado {
       width: 100%;
       display: flex;
       justify-content: space-around;
       align-items: center;
       padding: 10px;
   }


   #contenedor_noautenticado {
       text-decoration: none;
       color: white;
       font-size: 17px;
       display: flex;
       justify-content: space-evenly;
       align-items: center;
       width: 100%;
   }


   #contenedor_rutas #rutas {
       text-decoration: none;
       color: white;
       font-size: 17px;
       display: flex;
       justify-content: center;
       align-items: center;
   }

   #rutas img {
       width: 2em;
   }


   #submenu {
       position: relative;
       display: block;
   }

   #submenu:hover #submenu-contenido {
       display: block;
       z-index: 1;
   }

   #submenu-contenido {
       display: none;
       position: absolute;
       z-index: 1;
       background-color: #111010;
       min-width: 160px;
       z-index: 1;
   }

   #submenu-contenido a {
       color: rgb(248, 248, 248);
       display: block;
       padding: 10px;
       text-decoration: none;
       font-size: 14px;
       z-index: 1;
   }

   #submenu-contenido a:hover {
       background: rgb(9, 143, 98);
       z-index: 1;
   }
</style>