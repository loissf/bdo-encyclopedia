<template>
  <div class="selector">
    <button @click="value -= 1" :disabled="minusDisabled">-</button>
    <input
      type="text"
      onkeypress="return event.charCode >= 48 && event.charCode <= 57"
      v-model="value"
      :disabled="disabled"
    />
    <button @click="value += 1" :disabled="plusDisabled">+</button>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from "vue";

const props = defineProps({
  min: Number,
  max: Number,
  modelValue: Number,
  disabled: Boolean,
});

const emits = defineEmits(["update:modelValue"]);

const value = ref(
  ((props.modelValue ?? 0) < (props.min ?? 0)
    ? props.min
    : (props.modelValue ?? 0) > (props.max ?? Infinity)
    ? props.max
    : props.modelValue) ?? 0
);

const plusDisabled = computed(
  () => props.disabled || value.value >= (props.max ?? Infinity)
);
const minusDisabled = computed(
  () => props.disabled || value.value <= (props.min ?? 0)
);

watch(value, (newValue) => {
  if (props.max != undefined && newValue > props.max) {
    value.value = props.max;
  } else if (props.min != undefined && newValue < props.min) {
    value.value = props.min;
  }
  if (typeof value.value === "string") {
    value.value = parseInt(value.value);
  }
  emits("update:modelValue", value.value);
});
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.selector {
  display: flex;
  flex-direction: row;

  @include flex-center-all;

  gap: 1rem;

  input[type="text"] {
    @include input-element;
    width: 3rem;
    text-align: center;
  }

  button {
    @include input-element;

    width: 2.5rem;
    height: 2.5rem;

    user-select: none;
  }
}
</style>
