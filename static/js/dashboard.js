
const ctx = document.getElementById("requestChart");

if (ctx) {

    new Chart(ctx, {

        type: "pie",

        data: {

            labels: chartLabels,

            datasets: [{

                data: chartData,

                backgroundColor: [

                    "#22c55e",   // Allowed
                    "#f59e0b",   // Sanitized
                    "#ef4444"    // Blocked

                ],

                borderColor: "#111827",

                borderWidth: 3,

                hoverOffset: 18

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            animation: {

                animateRotate: true,

                animateScale: true,

                duration: 1500,

                easing: "easeOutQuart"

            },

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        color: "#e5e7eb",

                        font: {

                            size: 14,

                            weight: "bold"

                        },

                        padding: 20

                    }

                },

                tooltip: {

                    backgroundColor: "#1f2937",

                    titleColor: "#ffffff",

                    bodyColor: "#ffffff",

                    borderColor: "#3b82f6",

                    borderWidth: 1,

                    cornerRadius: 8,

                    padding: 12,

                    callbacks: {

                        label: function(context) {

                            return context.label + ": " + context.raw;

                        }

                    }

                }

            }

        }

    });

}