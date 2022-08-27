<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <NavbarView/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NavbarView from "../components/NavbarView.vue"; // @ is an alias to /src

export default defineComponent({
  name: "NavbarView",
  components: { NavbarView },
});
</script>
