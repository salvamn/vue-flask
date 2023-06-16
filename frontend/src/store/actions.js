import axios from 'axios';

const actions = {
  async crearUsuario({ commit }, usuario) {
    try {
      const response = await axios.post('http://localhost:5000/crear_usuario', usuario);
      commit('agregarUsuario', response.data.respuesta);
      
      return response.data.respuesta;
    } catch (error) {
      console.error('Error al crear el usuario:', error);
      throw error;
    }
  },
};






export default actions;
