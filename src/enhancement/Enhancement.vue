<template>
  <!-- <EnhancementView :enhancement="enhancement" /> -->
  <button @click="openModalClick()">BUTTON</button>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Enhancement } from "./Process";

import { useModal } from "@/components/modal/use-modal";
import ItemSelectModal from "./ItemSelectModal.vue";
const { openModal } = useModal();

async function openModalClick() {
  const result = await openModal<boolean>(ItemSelectModal);
}

const enhancement = ref<Enhancement>(
  new Enhancement(
    [
      {
        id: 14019,
        name: "Laytenn's Power Stone",
        grade: 3,
        enhancement: 0,
        quantity: 1,
      },
    ],
    [
      {
        id: 14019,
        name: "Laytenn's Power Stone",
        grade: 3,
        enhancement: 4,
        quantity: 1,
      },
    ],
    {
      id: 14019,
      name: "Laytenn's Power Stone",
      grade: 3,
      enhancement: 3,
      quantity: 1,
    },
    45
  )
);
</script>

<style scoped lang="scss"></style>
