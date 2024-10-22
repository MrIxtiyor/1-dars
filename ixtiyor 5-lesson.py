{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRMcWo0qcaauTF8ARteoC7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MrIxtiyor/1-dars/blob/main/ixtiyor%205-lesson.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "StvmeBqkSdmN",
        "outputId": "e32011e0-af7f-4edd-b356-a4cd45598f33"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1D Massiv:  [1 2 3 4 5]\n",
            "2D Massiv:\n",
            " [[1 2 3]\n",
            " [4 5 6]]\n",
            "Massivlar yig'indisi:  15\n",
            "O'rtacha:  3.0\n",
            "Ko'paytma:  120\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "# 1. Massiv yaratish\n",
        "array_1d = np.array([1, 2, 3, 4, 5])\n",
        "array_2d = np.array([[1, 2, 3], [4, 5, 6]])\n",
        "\n",
        "# 2. Matematik operatsiyalar\n",
        "sum_array = np.sum(array_1d)\n",
        "mean_array = np.mean(array_1d)\n",
        "product_array = np.prod(array_1d)\n",
        "\n",
        "print(\"1D Massiv: \", array_1d)\n",
        "print(\"2D Massiv:\\n\", array_2d)\n",
        "print(\"Massivlar yig'indisi: \", sum_array)\n",
        "print(\"O'rtacha: \", mean_array)\n",
        "print(\"Ko'paytma: \", product_array)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "# 1. Massiv yaratish\n",
        "array_1d = np.array([1, 2, 3, 4, 5])\n",
        "array_2d = np.array([[1, 2, 3], [4, 5, 6]])\n",
        "\n",
        "# 2. Matematik operatsiyalar\n",
        "sum_array = np.sum(array_1d)\n",
        "mean_array = np.mean(array_1d)\n",
        "product_array = np.prod(array_1d)\n",
        "\n",
        "print(\"1D Massiv: \", array_1d)\n",
        "print(\"2D Massiv:\\n\", array_2d)\n",
        "print(\"Massivlar yig'indisi: \", sum_array)\n",
        "print(\"O'rtacha: \", mean_array)\n",
        "print(\"Ko'paytma: \", product_array)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_Ys_N2zISh9j",
        "outputId": "093ec946-1b14-458e-f881-9de4f47480d4"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1D Massiv:  [1 2 3 4 5]\n",
            "2D Massiv:\n",
            " [[1 2 3]\n",
            " [4 5 6]]\n",
            "Massivlar yig'indisi:  15\n",
            "O'rtacha:  3.0\n",
            "Ko'paytma:  120\n"
          ]
        }
      ]
    }
  ]
}