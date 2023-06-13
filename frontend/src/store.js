import { createStore } from 'vuex';
import axios from 'axios';
const store = createStore({
  state() {
    return {
      publicaciones: [], // Estado de publicaciones en este caso lo dejamos vacío
      usuarios: [],
    }
  },
  mutations: {
        agregarPublicacion(state, publicacion){     // función de agregar publicación
            state.publicaciones.push(publicacion);  // va de la mano de publicaciones a publicación         
        },
        agregarUsuario(state, usuario){
            state.usuarios.push(usuario);
        }
  },
  actions: {
    crearusuario({ commit }, usuario) {
      return axios.post('http://127.0.0.1:5000/crear_usuario', usuario)
        .then(response => {
          commit('agregarUsuario', response.data);
          return response.data;
        })
        .catch(error => {
          console.error('Error al crear el usuario:', error);
          throw error;
        });
    }
  }
});



export default store;
