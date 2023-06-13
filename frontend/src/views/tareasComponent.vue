<template>
    <section id="contenedor_conjunto">

        <div id="contenedor_top_tareas">

            <!--<publicacion/>-->

        </div>


        <div id="contenedor_top_bottom">

          
                <form @submit.prevent="crearusaurio">

                    <label for="nombre">nombre</label>
                    <input type="text" v-model="nombre" id="nombre">
                    <label for="email">email</label>
                    <input type="text" v-model="email" id="email">
                    <label for="email">nombre_usuario</label>
                    <input type="text" v-model="nombre_usuario" id="email">
                    <label for="email">contraseña</label>
                    <input type="text" v-model="contraseña" id="email">
                    <button type="submit">crear usuario</button>

                </form>
           

        </div>

    </section>
</template>






<script>
//import publicacion from '@/components/publicacionComponent.vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();

    const crearusaurio = (usuario) => {
      store.dispatch('crearUsuario', usuario)
        .then(respuesta => {
          console.log('usuario creado:', respuesta);
        })
        .catch(error => {
          console.error('error al crear el usuario', error);
        });
    };

    return {
      crearusaurio
    };
  }
}
</script>






<style scoped>
#contenedor_top_bottom{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: red;
}
form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    color: black;
}
form input{
    color: black;
}
#contenedor_conjunto {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

#contenedor_top_tareas {
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>