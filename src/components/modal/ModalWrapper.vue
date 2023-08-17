<template>
  <div class="modal-background">
    <div class="modal-wrapper">
      <component :is="component" @close="closeModal" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const component = ref<unknown>();
const closeModal = ref<() => void>();
</script>

<style lang="scss">
#modal {
  z-index: 1000;

  height: 100vh;
  width: 100vw;

  position: absolute;

  overflow: hidden;

  top: 0;
  left: 0;

  .modal-background {
    height: 100%;
    width: 100%;

    background-color: rgba(0, 0, 0, 0.2);

    .modal-wrapper {
      height: min-content;
      width: min-content;

      position: relative;

      top: 50vh;
      left: 50vw;

      transform: translate(-50%, -50%);
    }
  }
}
</style>
