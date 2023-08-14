<template>
  <div class="enhancement-view">
    <ItemDisplay :item="enhancement.base" class="base-item" />
    <div class="arrow-container">
      <span>{{ enhancement.failstack }} fs</span>
      <p class="arrow">&darr;</p>
      <span>{{ chance?.toPrecision(4) }}%</span>
    </div>
    <ItemDisplay :item="enhancement.results[0]" class="result-item" />
  </div>
</template>
<script setup lang="ts">
import { Enhancement } from "./Process";
import ItemDisplay from "./ItemDisplay.vue";
import { ref } from "vue";
import { getEnhancementChance } from "@/queries";

const props = defineProps({
  enhancement: {
    type: Enhancement,
    required: true,
  },
});

const chance = ref<number>();

getEnhancementChance(
  props.enhancement.base.id,
  props.enhancement.base.enhancement,
  props.enhancement.failstack
).then((value = 0) => (chance.value = value * 100));
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.enhancement-view {
  display: flex;

  flex-direction: column;

  align-items: center;
  justify-content: center;

  .arrow-container {
    display: flex;
    flex-direction: row;

    align-items: center;

    margin: 1rem;

    span {
      width: 3rem;

      padding: 0.5rem 1rem;

      border: 1px solid rgb(80, 80, 80);

      border-radius: 12px;

      background-color: #2b2b2b;
      box-shadow: 4px 4px 12px 0px rgba(0, 0, 0, 0.75);
    }

    .arrow {
      font-size: 200%;
      margin: 0 0.5rem;

      padding: 0 1rem;
    }
  }

  .base-item {
    border: 1px solid rgb(170, 170, 170);
  }

  .result-item {
    opacity: 0.5;

    border: 1px dashed rgb(170, 170, 170);
  }
}
</style>
