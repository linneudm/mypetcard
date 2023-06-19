<script setup lang="ts">
// import { ref } from 'vue'
</script>

<template>
  <div class="root-login">
    <h1>Login View</h1>
    <form class="form-login">
      <div class="input-group">
        <label
          for="username"
          class="label-input"
        >Username</label>
        <input
          id="username"
          type="text"
          class="input-text"
        >
      </div>
      <div class="input-group">
        <label
          for="password"
          class="label-input"
        >Password</label>
        <input
          id="password"
          type="password"
          class="input-text"
        >
      </div>
      <button class="login-submit">
        Login
      </button>
    </form>
  </div>
</template>

<style lang="less">
  @blue: #175EA8;
  @yellow: #F9E6B3;
  :root{
    color: #fff;
    background-color: @blue;
    justify-content: center;
  }
  .root-login{
    font-family: 'Varela Round', sans-serif;

    width: 330px;
    & h1{
      text-align: center;
    }
    .login-submit{
      margin-top: 24px;
      display: flex;
      width: 100%;
      border: none;
      padding: 12px;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      border-radius: 8px;
      background-color: @blue;
      border: 2px solid #fff;
      color: #fff;
      font-family: 'Varela Round', sans-serif;
      &:hover{
        transition: 0.3s;
        background-color: #fff;
        color: @blue;
      }
    }
  }
  .form-login .input-group{
    display: flex;
    flex-direction: column;
    & input{
      flex: 1;
      font-weight: bold
    }
    & label {
      flex: 1;
      font-weight: bold;
      padding: .5em 1em .5em 0;
    }
  }

</style>
