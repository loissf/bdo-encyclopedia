import { createApp, defineComponent, ref } from "vue";
import vue from "vue";
import ModalWrapper from "./ModalWrapper.vue";

const app = ref<vue.App<Element>>();
const promiseResolve = ref<(value: any) => void>();

function openModal<T>(component: Object): Promise<T> {
  const instance = defineComponent({
    extends: ModalWrapper,
    setup: () => {
      return {
        component: component,
        closeModal: closeModal,
      };
    },
  });

  app.value = createApp(instance);

  const modalWrapper = document.createElement("div");
  modalWrapper.id = "modal";

  document.body.appendChild(modalWrapper);

  app.value?.mount(modalWrapper);

  return new Promise<T>((resolve) => (promiseResolve.value = resolve));
}

function closeModal(result: any) {
  const modalWrapper = document.querySelector("body > #modal");
  if (modalWrapper) {
    document.body.removeChild(modalWrapper);
  }

  app.value?.unmount();

  if (promiseResolve.value) {
    promiseResolve.value(result);
  }
}

export function useModal() {
  return {
    openModal,
    closeModal,
  };
}
