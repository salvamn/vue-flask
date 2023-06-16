const mutations = {
    agregarUsuario(state, usuario) {
      state.usuarios.push(usuario);
    },
    establecerUsuarioConectado(state, value){
      state.UsuarioConectado = value;
    }
};
  
  export default mutations;
  