import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      publicaciones: [], // Estado de publicaciones en este caso lo dejamos vacío
    }
  },
  mutations: {
        agregarPublicacion(state, publicacion){     // función de agregar publicación
            state.publicaciones.push(publicacion);  // va de la mano de publicaciones a publicación         
        }
    }
});

export default store;
